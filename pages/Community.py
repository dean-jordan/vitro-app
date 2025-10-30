from openai import OpenAI
import streamlit as st

st.title("The Vitro Community")
st.caption("See the genomes others have created and contribute to the open research community.")

st.form(
    key="form1",
    clear_on_submit="True",
    enter_to_submit=True,
    border=True,
)

st.text_area(
    label="Name",
    key="form1"
)

st.text_area(
    label="Post Title",
    key="form1"
)

st.text_area(
    label="Generated Prefix",
    key="form1"
)

st.text_area(
    label="Additional Generated Materials",
    key="form1"
)

st.text_area(
    label="Description of Findings/Problem",
    key="form1"
)

st.form_submit_button(
    label="Submit",
    key="form1"
)