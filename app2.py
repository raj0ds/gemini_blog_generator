import streamlit as st
import google.generativeai as genai
import os
import textwrap
from IPython.display import Markdown
from IPython.display import display


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)).data

def getllamaresponse(input_text, no_words, blog_style, gemini_api):
    os.environ["GOOGLE_API_KEY"] = gemini_api
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')
    prompt=f'Write a blog for {blog_style} job profile for a topic {input_text} within {no_words}'
    response = model.generate_content(prompt)
    response_text= to_markdown(response.text)
    response=response.text
    # print(response)
    return response

st.set_page_config(page_title="Rajeev Blog Generating website",
                   page_icon=":robot_face:",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Rajeev blog :robot_face: ")
input_text = st.text_input("Enter the blog Topic")

# Creating two more columns for additional fields

col1, col2, col3 = st.columns([2.5,2.5, 5])
with col1:
    no_words = st.text_input("Enter number of words")
with col2:
    blog_style=st.selectbox('Writing the blog for', ('Data Scientist', 'Data Analyst', 'Researcher', 'Common people', 'Developers'), index=0)
with col3:
    gemini_api= st.text_input("Please Enter your Gemini API")
submit=st.button("Generate blog")
if submit:
    st.write(getllamaresponse(input_text, no_words, blog_style,gemini_api))
