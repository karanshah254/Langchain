from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# Prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}"),
    ]
)

# streamlit framework
st.title("Llama2 Chatbot API")
input_text = st.text_input("Enter your question here:")


# ollama llama2 LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt_template | llm | output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))
