import streamlit as st

st.title("The Vitro Community")
st.caption("See the genomes others have created and contribute to the open research community.")

with st.form(key="form1", clear_on_submit=True):
    name = st.text_input(label="Name", key="name")
    post_title = st.text_input(label="Post Title", key="post_title")
    gen_prefix = st.text_area(label="Generated Prefix", key="gen_prefix")
    additional = st.text_area(label="Additional Generated Materials", key="additional")
    description = st.text_area(label="Description of Findings/Problem", key="description")
    submitted = st.form_submit_button(label="Submit")

    if submitted:
        st.success("Thank you — your post has been submitted.")