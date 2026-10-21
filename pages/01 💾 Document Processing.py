import ollama
import streamlit as st
import pdfplumber
import pandas as pd
import streamlit_pdf
import time

st.header("Document Upload and Processing")
st.write("""
        Here you can upload your business documents (e.g. Bills). Use the expander to double-check
        your file and to save it to the database.
        """)

st.divider()

# File upload. Program can display the file either as Image or as Text.

file_upload = st.file_uploader(label="Upload document(s)", type=".pdf")

if file_upload is not None:

    bytes_data = file_upload.getvalue()

    # Only if the uploaded File indeed is a .pdf-file.
    if bytes_data.startswith(b'%PDF-'):
        try:
            with pdfplumber.open(file_upload) as pdf:
                pages_text = []
                pages_images = []

                for page in pdf.pages:
                    text = page.extract_text()
                    image = page.to_image(resolution=250).original
                    pages_images.append(image)
            
                    if text:
                        pages_text.append(text)

                sum_text = ("\n".join(pages_text))

                if sum_text.strip():
                    st.success(f"{file_upload.name} successfully uploaded!")
        
                    with st.expander(label="Expand file", expanded=True):
                        page_number = st.pagination(num_pages=len(pages_images), width="stretch") # Blättern mit Images
                        st.image(image=pages_images[page_number - 1], width="stretch") # Anzeige mit Image des PDFs
                        #page = st.pagination(num_pages=len(pages_text), width="stretch") # Blättern mit angezeigtem Text/Code
                        #st.code(pages_text[page - 1])
                        #st.code(sum_text) # Anzeige mit purem Text
                        #st.pdf(file_upload, height="stretch") # Anzeige mit Original-PDF
                        file_to_database = st.button("Save file to database")   
                    # DATABASE EINBINDEN
                    if file_to_database:
                        with st.status("Preparing Database", expanded=False, type="step"):
                            st.write("Database found")
                            time.sleep(2)
                        with st.status("Processing informations", expanded=False, type="step"):
                            st.write("Saving file")
                            time.sleep(2)

                        st.status("File successfully saved", state="complete", type="step")
                           
                if sum_text == "":
                    st.error("PDF is empty!")
        except OSError:
            st.error(f"{file_upload.name} is damaged or you do not have the permission to open!")
else:
    st.warning("No document uploaded!")

# Ab hier KI Agent: Liest bestimmte Bereiche der hochgeladenen PDFs aus, wertet sie aus und kann
# eigenständig KPIs daraus ableiten. Evtl. mit Diagrammen/Vorhersagen?

