from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv() 

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app= FastAPI(
    title="Langchain Server",
    version='1.0',
    description="API server"
)


#ollama
llm= Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("write a poem of 100 words on {topic}")
prompt2=ChatPromptTemplate.from_template("write a paragrapgh of 100 words on {topic}")

add_routes(
    app,
    prompt1|llm,
    path="/poem"
)

add_routes(
    app,
    prompt2|llm,
    path="/paragraph"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
