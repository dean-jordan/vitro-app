from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[Visualize with AlphaFold 3](https://alphafoldserver.com)"
    "[Develop DNA with Evo 2](https://arcinstitute.org/tools/evo/evo-designer)"

st.title("Information Assistant")
st.caption("Help on generating your description and working within biological constraints.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What can I help you with?"}]

# render chat messages (skip system messages)
for msg in st.session_state.messages:
    if msg.get("role") == "system":
        continue
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        model="ft:gpt-4.1-nano-2025-04-14:personal:nucleotide-primer:CVuPZNqP",
        messages=st.session_state.messages
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
