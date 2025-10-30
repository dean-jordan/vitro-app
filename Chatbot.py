from openai import OpenAI
import streamlit as st

# Replace this with your OpenAI-published system prompt ID
_SYSTEM_PROMPT_ID = "pmpt_690202529f6081938bb6e11ba2d4d7890d5fa374437759f3"

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("Vitro")
st.caption("As of now, there are a variety of machine learning methods to create DNA. However, they all require DNA primers as input. This model allows for a DNA primer to be generated from natural language.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Describe a cell/organism."}]

# render chat messages (do not render the system prompt)
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # send the published system prompt ID to the API (do not include the system content in the UI)
    messages_for_api = st.session_state.messages

    response = client.chat.completions.create(
        model="ft:gpt-4.1-nano-2025-04-14:personal:nucleotide-primer:CVuPZNqP",
        messages=messages_for_api,
        system_prompt={"id": _SYSTEM_PROMPT_ID},
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
