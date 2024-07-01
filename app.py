from dotenv import load_dotenv


load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model - genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(input, pdf_content[0], prompt)
    return response.text

def input_pdf_setup(uploaded_file):
    
    if uploaded_file is not None:
        # convert pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file)
        
        first_page = images[0]
        
        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(), #encode to base64
            }
        ]
        
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
## Streamlit app

st.set_page_config(page_title="Resume Summarizer", page_icon=":guardsman:", layout="wide")
st.header("Resume Summarizer")
st.subheader("Upload your resume to get a summary")
input_text = st.text_area("Job Description: ", key= "input")
uploaded_file = st.file_uploader("Upload Resume in PDF format", type=["pdf"], key="uploaded_file")


if uploaded_file is not None:
    st.write("PDF upload successful")
    
submit1 = st.button("Generate Summary")

submit2 = st.button("Skills to improve")

submit3 = st.button("Skills to learn")

submit4 = st.button("Match")


input_prompt = """


"""