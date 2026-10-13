import ollama
import streamlit as st

st.header("AI Integration")
st.write("""
        This is a placeholder.
        """)

st.divider()

user_input = st.text_input("Ask AI")

answer = st.button("Generate answer")
if answer:
    with st.spinner("Generatering answer ..."):
        response = ollama.chat(model="llama3.1", messages=[
            {"role": "user",
            "content": f"Give an answer about the user's input {user_input}. Keep yourself SHORT to maximize speed performance."
            }
        ])

    st.text_area(label="", value=response["message"]["content"], height="stretch", label_visibility="visible")

# message = st.chat_message("assistant")
# uploads = st.chat_input(
# "Upload your PDF document(s)",
# accept_file=True,
# file_type=["pdf"])
# 
# AI Agent für späteres Auswerten der Daten?

# Verlauf des Chats muss sichtbar sein, Verlauf des KI Agenten muss sichtbar sein, was dessen einzelne Schritte waren