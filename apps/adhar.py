import streamlit as st
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
import cv2
import numpy as np
from PIL import Image
import tempfile
import re


def app():

    try:
        img_location = st.file_uploader("upload file")
        BINARY_THREHOLD = 180

        size = None
        def get_size_of_scaled_image(im):
            global size
            if size is None:
                length_x, width_y = im.size
                factor = max(1, int(IMAGE_SIZE / length_x))
                size = factor * length_x, factor * width_y
            return size

        def process_image_for_ocr(file_path):
            temp_filename = set_image_dpi(file_path)
            im_new = remove_noise_and_smooth(temp_filename)
            return im_new

        def set_image_dpi(file_path):
            im = Image.open(file_path)
            # size = (1800, 1800)

            im_resized = im
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
            temp_filename = temp_file.name
            im_resized.save(temp_filename, dpi=(300, 300))  # best for OCR
            return temp_filename

        def image_smoothening(img):
            ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
            ret2, th2 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            blur = cv2.GaussianBlur(th2, (1, 1), 0)
            ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            return th3

        def remove_noise_and_smooth(file_name):
            img = cv2.imread(file_name, 0)
            filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
                                             41,
                                             3)
            kernel = np.ones((1, 1), np.uint8)
            opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
            img = image_smoothening(img)
            or_image = cv2.bitwise_or(img, closing)
            return or_image

        image = process_image_for_ocr(img_location)
        test_english = pytesseract.image_to_string(image)
        test_marathi = pytesseract.image_to_string(image, lang='mar')

        def extract_name(text):
            pattern_to_extract_name = '[A-Z]?[a-z]{2,}[A-Za-z]*\s[A-Z]?[a-z]{3,}[A-Za-z]*\s[A-Z]?[a-z]{2,}[A-Za-z]*'
            extracted_name = re.search(pattern_to_extract_name, text)
            name = extracted_name.group()
            return name

        def adhars(adhar_no_e, adhar_no_m):
            if adhar_no_e == adhar_no_m:
                return adhar_no_e
            else:
                return adhar_no_m

        def extract_adhar_no(text_e, text_m):
            adhar = "0000 0000 0000"
            pattern_to_extract_ = '[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}'
            extracted_adhar_no_e = name = re.search(pattern_to_extract_, text_e)
            extracted_adhar_no_m = name = re.search(pattern_to_extract_, text_m)
            if extracted_adhar_no_e:
                adhar_no_e = extracted_adhar_no_e.group()
            else:
                adhar_no_e = None
            if extracted_adhar_no_m:
                adhar_no_m = extracted_adhar_no_m.group()
            else:
                adhar_no_m = None

            if adhar_no_e != None and adhar_no_m != None:
                adharno = adhars(adhar_no_e, adhar_no_m)
                return adharno

            elif adhar_no_m == None and adhar_no_e != None:
                return adhar_no_e
            elif adhar_no_m != None and adhar_no_e == None:
                return adhar_no_m
            else:
                return adhar

        def extract_gender(text_e):
            g = "Male"
            pattern_to_extract_gender = 'male|Male|MALE|female|Female|FEMALE'
            extracted_gender = re.search(pattern_to_extract_gender, text_e)
            if extracted_gender:
                gender = extracted_gender.group()
                return gender
            else:
                return g

        def extract_dob(test_e):
            ddate = "00/00/0000"
            pattern_date = '(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}'
            extracted_date_birth = re.search(pattern_date, test_e)
            if extracted_date_birth:
                date = extracted_date_birth.group()
                return date
            else:
                pattern_when_no_full_date = '(\s|:)*(19[6789]\d|20[012]\d)'
                date_birth = re.search(pattern_when_no_full_date, test_e)
                date1 = date_birth
                if date1:
                    date2 = dateob(date1)
                    return date2
                else:
                    return ddate

        def dateob(date1):
            if date1:
                date = date1.group()
                date = re.sub('[\W_]+', '', date)
                return date

        def fdate(date):
            if date == '00/00/0000':
                dates = extract_dob(test_marathi)
                return dates
            else:
                return date

        Name = extract_name(test_english)
        f_date = extract_dob(test_english)
        Date = fdate(f_date)
        AdharNumber = extract_adhar_no(test_english, test_marathi)
        Gender = extract_gender(test_english)

        st.header("details")
        st.write("Name of person :", Name)
        st.write("Date of birth :", Date)
        st.write("Adhar card number :", AdharNumber)
        st.write("Gender :", Gender)
    except AttributeError:
        print("There is no such attribute")


