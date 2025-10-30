from openai import OpenAI
import streamlit as st

st.title("Information")
st.caption("About the App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.header("Synthetic DNA Engineering with Vitro")

st.text("")

st.header("AlphaFold 2/AlphaFold 3 Integration")

st.text("")

st.header("Use of Prefixes for Evo/Evo 2")

st.text("")