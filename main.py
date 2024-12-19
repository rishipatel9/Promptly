from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def get_response(prompt: str): 
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'), temperature=0.5)  
    response = llm(prompt)
    return response
    
st.set_page_config(page_title="Q&A", page_icon="🔗", layout="wide")
st.header('Q&A')

input_text = st.text_input("Input", key="input")
submit = st.button("Ask the Question")

if submit and input_text: 
    response = get_response(input_text)
    st.subheader("The Response is:")
    st.write(response)
