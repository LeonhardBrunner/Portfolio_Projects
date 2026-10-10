import ollama
import streamlit as st
import pdfplumber
import pandas as pd
import streamlit_pdf as stp

st.header("Document Upload and Processing")
st.write("""
        Here you can upload your business documents (e.g. Bills). Use the expander to double-check
        your file and save it to the database.
        """)

st.divider()

# File upload

file_upload = st.file_uploader(label="Upload document(s)", type=".pdf")

if file_upload is not None:

    bytes_data = file_upload.getvalue()

    if bytes_data.startswith(b'%PDF-'):
        try:
            with pdfplumber.open(file_upload) as pdf:
                pages_text = []

                for page in pdf.pages:
                    text = page.extract_text()
            
                    if text:
                        pages_text.append(text)
                
                sum_text = ("\n".join(pages_text))

                if sum_text.strip():
                    st.success(f"{file_upload.name} successfully uploaded!")
        
                    with st.expander(label="Expand file", expanded=True):
                        page = st.pagination(num_pages=len(pages_text), width="stretch")
                        st.code(pages_text[page - 1])
                        #st.code(sum_text) # Anzeige mit purem Text
                        #st.pdf(file_upload, height="stretch") # Anzeige mit Original-PDF
                        file_to_database = st.button("Save file to database") # Button verbinden mit Database

                if sum_text == "":
                    st.error("PDF is empty!")

        except OSError:
            st.error(f"{file_upload.name} is damaged or you do not have the permission to open!")

else:
    st.warning("No document uploaded!")


    


