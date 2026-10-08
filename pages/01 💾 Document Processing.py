import ollama
import streamlit as st
import pdfplumber
import pandas as pd

st.title("Document Upload and Processing")
st.write("""
        Here you can upload your business documents (e.g. Bills). After checking the document for it's correctness, you can
        save the document in the database for AI Processing.
        """)

file_upload = st.file_uploader(label="Upload document(s)", type=".pdf")
if file_upload is not None:
    
    if file_upload.name.lower().endswith(".pdf"):
        st.success(f"{file_upload.name} successfully uploaded!")
    
    else:
        st.error("Error! Incorrect format. Transform document to PDF!")    

with st.form("My_Form"):
    
    if file_upload is not None:
        with pdfplumber.open(file_upload) as pdf:

            for page in pdf.pages:
                st.write(page.extract_text())
    else:
        st.error("No document uploaded!")

submit_document_to_databse = st.button("Save document in database")

