import streamlit as st
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
import cv2
import numpy as np
from PIL import Image
import tempfile
import re

def app():
    img_location = st.file_uploader("upload file")
    try:
        def process_image_for_ocr(file_path):
            temp_filename = set_image_dpi(file_path)
            return temp_filename

        def set_image_dpi(file_path):
            im = Image.open(file_path)
            im_resized = im
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
            temp_filename = temp_file.name
            im_resized.save(temp_filename)  # best for OCR
            return temp_filename

        loc = process_image_for_ocr(img_location)
        # st.write(loc)

        image = cv2.imread(loc, 0)
        test_english = pytesseract.image_to_string(image)

        def get_info(test_english):
            clean_test = test_english.replace('INCOME', '$').replace('DEPARTMENT', '$').replace("INDIA", "$ ").replace(
                "&",
                "$").replace(
                "GOVT", '$').replace("OF", "$").replace("Permanent", "$").replace("Account", "$").replace("Number",
                                                                                                          "$").replace(
                "'",
                "$")
            new_string = re.sub(r"[a-z]", "$", clean_test)
            final_string = re.sub('[!,*)@#%($_?.^]', '$', new_string)
            list1 = []
            list5 = []
            list7 = []
            for i in range(len(final_string)):
                if final_string[i] == "\n":
                    list1.append(i)

            for i in range(len(list1) - 2):
                start = list1[i]
                end = list1[i + 1]
                stri = final_string[start:end]
                if len(stri) > 4:
                    list5.append(stri[1:])

            for i in list5:
                if i.count("$") < 2:
                    j = re.sub('[!,*)@#%($_?.^]', '', i)
                    list7.append(j)
            return list7

        info = get_info(test_english)
        Name = info[0]
        Dad_name = info[1]
        Date = info[2]
        Pan_number = info[3]

        st.header("details")
        # st.write(Name)
        # st.write(Dad_name)
        # st.write(Date)
        # st.write(Pan_number)
        st.write("Name of person :", Name)
        st.write("Father Name :", Dad_name)
        st.write("Pan card number :", Pan_number)
        st.write("Date of Birth :", Date)

    except AttributeError:
        print("please upload image first")







