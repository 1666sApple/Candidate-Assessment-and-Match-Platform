from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
import base64
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(input, pdf_content[0], prompt)
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode(),
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Resume Summarizer", page_icon=":guardsman:", layout="wide")
st.header("Resume Summarizer")
st.subheader("Upload your resume to get a summary")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Resume in PDF format", type=["pdf"], key="uploaded_file")

if uploaded_file is not None:
    st.write("PDF upload successful")

submit1 = st.button("Generate Summary")
submit2 = st.button("Skills to improve")
submit3 = st.button("Skills to learn")
submit4 = st.button("Match")

input_prompt1 = """
You are an experienced technical Human Resource Manager who possesses good technical knowledge of any one of the following: Data Science, Full Stack Web Development, Big Data Engineering, Devops, MLops or Data Analyst.
You are tasked with summarizing a resume for a job applicant that are provided. Please share your professional evaluation on whether the applicant is a good fit for the role.
Moreover, highlight the skills that the applicant needs to improve and the skills that the applicant needs to learn. Also, mention the strength that the applicant has in relation to the specified task.
"""

input_prompt2 = """
Highlight the skills the applicant needs to improve to enhance their candidacy for the role of a job applicant based on their resume and job description provided.
"""

input_prompt3 = """
Identify and highlight the crucial skills the applicant needs to learn for the role of a job applicant based on their resume and job description provided.
"""

input_prompt4 = """
Evaluate the applicant's fit for the role based on their resume and job description provided, and emphasize the applicant's strengths that are particularly relevant to the task.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Here's your summary:")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Skills to Improve:")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Skills to Learn:")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")

if submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("Match Evaluation:")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")
