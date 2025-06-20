import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})
    print(response)

    return response.json()['output']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/paragraph/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an poem on")
input_text1=st.text_input("Write a paragraph on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))