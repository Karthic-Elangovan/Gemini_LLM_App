from dotenv import load_dotenv
load_dotenv() ## loading all the environment vatriables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

## function to load the gemini pro model and get the responses

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

## initialize our streamlit app

st.set_page_config(page_title ="Gemini Q & A Demo")

st.header("Generative LLM Application")

input = st.text_input("Input: ",key = "input")

submit = st.button("Ask the question")

## when submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
     