from openai import OpenAI
import streamlit as st

PUBLISHED_PROMPT_ID = "pmpt_6902e2b7e4d081938750c0f347bddb8202e5a84e628db026"

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("Vitro")
st.caption("As of now, there are a variety of machine learning methods to create DNA. However, they all require DNA primers as input. This model allows for a DNA primer to be generated from natural language.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Describe a cell/organism."}]

# render chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

def _extract_prompt_run_text(resp):
    # Try common locations for the textual output from prompts.run
    try:
        # object-like response
        output = getattr(resp, "output", None) or resp.get("output") if isinstance(resp, dict) else None
        if output and len(output) > 0:
            first = output[0]
            if isinstance(first, dict):
                content = first.get("content")
                if isinstance(content, list) and len(content) > 0:
                    part = content[0]
                    if isinstance(part, dict) and "text" in part:
                        return part["text"]
        # fallback property names
        if hasattr(resp, "output_text"):
            return resp.output_text
    except Exception:
        pass
    # final fallback to string representation
    return str(resp)

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Run the published prompt. Provide the user's input and the conversation history as inputs.
        response = client.prompts.run(
            prompt=PUBLISHED_PROMPT_ID,
            input={
                "user_input": prompt,
                "conversation": st.session_state.messages,
            },
        )

        msg = _extract_prompt_run_text(response)
    except Exception as e:
        msg = f"Error calling prompt: {e}"

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
