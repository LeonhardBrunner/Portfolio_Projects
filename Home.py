import streamlit as st
import pandas as pd
import ollama

st.set_page_config(page_title= "Placeholder", layout= "wide", page_icon= "🚀")

st.title("Placeholder")
st.write("""
        This App will include different Tools and Metrics for **Business and IT Purposes**. Included are:
        - Business Analyse Tools
        - IT-Performance Checks
        - Document Upload Tool
        - AI Integration Tool
        
        
        To navigate, use the sidebar on the left.
        """)

#st.selectbox("Select:", ("Thing A", "Thing B", "Thing C"))