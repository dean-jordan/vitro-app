import streamlit as st
from datetime import datetime

st.title("The Vitro Community")
st.caption("See the genomes others have created and contribute to the open research community.")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Visualize with AlphaFold 3](https://alphafoldserver.com)"
    "[Develop DNA with Evo 2](https://arcinstitute.org/tools/evo/evo-designer)"

# Initialize posts store in session state
if "posts" not in st.session_state:
    st.session_state["posts"] = []

with st.form(key="form1", clear_on_submit=True):
    name = st.text_input(label="Name", key="name")
    post_title = st.text_input(label="Post Title", key="post_title")
    gen_prefix = st.text_area(label="Generated Prefix", key="gen_prefix")
    additional = st.text_area(label="Additional Generated Materials", key="additional")
    description = st.text_area(label="Description of Findings/Problem", key="description")
    submitted = st.form_submit_button(label="Submit")

    if submitted:
        post = {
            "name": name,
            "title": post_title,
            "gen_prefix": gen_prefix,
            "additional": additional,
            "description": description,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }
        st.session_state["posts"].append(post)
        st.success("Thank you — your post has been submitted.")

st.markdown("---")
st.header("Submitted Posts")

posts = list(reversed(st.session_state.get("posts", [])))  # newest first

if not posts:
    st.info("No posts yet. Be the first to submit!")
else:
    for i, p in enumerate(posts, start=1):
        st.subheader(f"{p.get('title') or 'Untitled'}")
        st.caption(f"By {p.get('name') or 'Anonymous'} — submitted {p.get('timestamp')}")
        if p.get("description"):
            st.markdown("**Description:**")
            st.write(p["description"])
        if p.get("gen_prefix"):
            st.markdown("**Generated Prefix:**")
            st.code(p["gen_prefix"], language="text")
        if p.get("additional"):
            st.markdown("**Additional Generated Materials:**")
            st.write(p["additional"])
        if i != len(posts):
            st.markdown("---")