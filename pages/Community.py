from openai import OpenAI
import streamlit as st

st.title("The Vitro Community")
st.caption("See the genomes others have created and contribute to the open research community.")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

