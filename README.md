# 🧾 Document Validator using OCR (Python + Streamlit)

## 📌 Project Description

This project is a **Document Validator** built entirely in **Core Python using OCR (Optical Character Recognition)**. It uses **Tesseract OCR** along with **Streamlit** to create an interactive web interface where users can upload images of identity documents (like Aadhaar and PAN cards). The app automatically extracts important information such as:

- Full Name  
- Date of Birth  
- Aadhaar Number or PAN Number  
- Gender  
- Father’s Name (in the case of PAN)

The project is a demonstration of how real-world document verification works using image processing and character recognition in a lightweight, Python-based application.

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – Web UI for uploading and displaying results
- **Tesseract OCR** (`pytesseract`) – For extracting text from documents
- **OpenCV** – For image noise reduction and thresholding
- **Pillow (PIL)** – For basic image manipulation
- **Regex** – To extract structured patterns like Aadhaar and dates

---

## 🚀 Features

- Upload Aadhaar or PAN card images
- Automatically extract relevant personal data
- Multilingual support (English and Marathi OCR)
- Noise removal and smoothing to improve OCR accuracy
- Pattern-based data validation using regular expressions
- Streamlit UI for quick preview of extracted data

---

## 🎓 Why I Built This

I created this project to **learn how OCR works in practical scenarios**, particularly for reading documents and verifying structured information from scanned images or photos.

Working with this helped me understand:

- How OCR can be leveraged to automate identity extraction  
- How to clean and prepare images for better recognition  
- How regex and simple logic can replace complex AI models for specific data formats

This project gave me a hands-on perspective on what happens behind the scenes in real-world applications like digital KYC, government ID validation, and mobile scanner apps.

---

## 🧠 Key Learnings

- Learned how to preprocess images for OCR using **OpenCV** (thresholding, blurring, morphology)
- Built multilingual OCR support with **pytesseract** (Marathi + English)
- Understood the structure of official IDs like Aadhaar and PAN, and how to extract reliable data from them
- Gained experience with **regex pattern matching** for extracting Aadhaar numbers, names, dates, and gender info
- Developed a complete working web interface using **Streamlit**

---

## 💻 How to Run the App

### 1. Install Dependencies

```bash
pip install streamlit pytesseract opencv-python pillow
```

### 2. Install Tesseract OCR Engine

Download and install Tesseract OCR from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).

Make sure to set the correct path in your Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

Upload a PAN or Aadhaar image and see the extracted results live on your browser.

---

## 📷 Supported Documents

✅ **Aadhaar Card** – Extracts name, DOB, Aadhaar number, and gender  
✅ **PAN Card** – Extracts name, father’s name, DOB, and PAN number

---

## 👨‍💻 Author

**Manish Shankar Jadhav**  
📧 Email: mn649712@dal.ca
