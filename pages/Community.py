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
    label="Name"
)

st.text_area(
    label="Post Title"
)

st.text_area(
    label="Generated Prefix"
)

st.text_area(
    label="Additional Generated Materials"
)

st.text_area(
    label="Description of Findings/Problem"
)

st.form_submit_button(
    label="Submit"
)