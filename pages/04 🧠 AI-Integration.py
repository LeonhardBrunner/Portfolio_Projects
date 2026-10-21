import ollama
import streamlit as st

st.header("AI Integration")
st.write("""
        This is a placeholder.
        """)

st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

with st.chat_message("assistant"):
    pass

st.chat_input("Ask me anything!")
    

#user_input = st.text_input("Ask AI")

#answer = st.button("Generate answer")
#if answer:
#    with st.spinner("Generatering answer ..."):
#        response = ollama.chat(model="llama3.1", messages=[
#            {"role": "user",
#            "content": f"Give an answer about the user's input {user_input}. Keep yourself SHORT to maximize speed performance."
#           }
#       ])
#
#    st.text_area(label="", value=response["message"]["content"], height="stretch", label_visibility="visible")



# AI Agent für späteres Auswerten der Daten?

# Verlauf des Chats muss sichtbar sein, Verlauf des KI Agenten muss sichtbar sein, was dessen einzelne Schritte waren