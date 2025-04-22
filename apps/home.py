import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

def app():
    st.title('Home')
    st.title("Document validator")
    st.markdown("This app uses OCR to get the details from the image.")
    st.markdown("we have used pytesseract ocr ")



