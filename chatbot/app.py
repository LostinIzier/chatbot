from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please respond to the user queries.")
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title('ChatBot0.0')
input_text=st.text_input("ask me something.")

#openAI llms
llm= ChatOpenAI(model="gpt-3.5-turbo")
output_parser= StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
