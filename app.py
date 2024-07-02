from dotenv import load_dotenv


load_dotenv()

import streamlit as st
import os
import io
import base64
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


input_prompt1 = """
You are an experienced technical Human Resource Manager who possesses good technical knowledge of any one of the following: Data Science, Full Stack Web Development, Big Data Engineering, Devops, MLops or Data Analyst.
You are tasked with summarizing a resume for a job applicant that are provided. Please share your professional evaluation on whether the applicant is a good fit for the role.
Moreover, highlight the skills that the applicant needs to improve and the skills that the applicant needs to learn. Also, mention the strength that the applicant has in relation to the specified task.
"""

input_prompt2 = """
As an experienced technical Human Resource Manager with expertise in Data Science, Full Stack Web Development, Big Data Engineering, DevOps, MLOps, and Data Analysis, your task is to thoroughly review and summarize a job applicant's resume. Provide a professional evaluation of the candidate's suitability for the role, based on their qualifications and experience. Highlight specific skills the applicant should improve to enhance their candidacy, as well as identify any critical skills they need to acquire for success in the position. Additionally, emphasize the applicant's core strengths that are particularly relevant to the specified task or role, showcasing how these strengths align with job requirements and could contribute to their effectiveness in the position. This comprehensive assessment should offer a balanced view of the candidate's current capabilities and their potential for growth, aiding in informed decision-making about their fit for the role and potential value to the organization.
"""
input_prompt3 = """
Version 1:
As a seasoned technical HR Manager with expertise spanning Data Science, Full Stack Development, Big Data, DevOps, MLOps, and Data Analysis, your role is to evaluate a job applicant's resume comprehensively. Assess the candidate's fit for the position, pinpoint skills needing improvement, identify crucial skills to be acquired, and highlight the applicant's strengths relevant to the role. Your analysis should provide a balanced view of the candidate's current abilities and growth potential, facilitating informed hiring decisions.
"""

input_prompt4 = """
As a seasoned technical Human Resource Manager with expertise in Data Science, Full Stack Web Development, Big Data Engineering, Devops, MLops, and Data Analysis, you've been assigned to review a job applicant's resume. Provide a professional assessment of the candidate's fit for the position. Your evaluation should also point out areas where the applicant needs skill improvement and what new skills they should learn. Lastly, emphasize the applicant's strengths that are particularly relevant to the task in question.
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
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Here's your summary:")
        st.write(response)
    else:
        raise FileNotFoundError("No file uploaded")
    
