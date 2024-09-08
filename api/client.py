# for all web and mobile apps
import requests
import streamlit as st


# Function to get response from Ollama API
def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}}
    )
    return response.json()["output"]


# Streamlit app
st.title("Ollama Poem Generator")
input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))
