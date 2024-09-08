# for all api's
# created a swagger documentation for the api

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain API",
    description="API for LangChain",
    version="1.0",
)

add_routes(app, ChatOpenAI(), path="/openai")

## Ollama Llama2
llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_template("Write a poem on {topic} for 5 year old child in 100 words")


add_routes(
    app,
    prompt | llm,
    path="/poem",
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
