from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    system_prompt = st.text_area(
        "System prompt",
        value='''
        You are a model that generates DNA sequence prefixes for input into downstream biological language models such as Evo 2.

        Your task:

        - Take as input a natural-language description of an organism, cell type, or phenotype.
        - Output only the beginning of a DNA sequence (nucleotides using A, T, C, G).
        - The output should resemble a realistic genetic construct or genomic segment relevant to the described organism.
        - You must not include any explanatory text, comments, or formatting—only the DNA sequence itself, on a single line.

        Output format:

        ATGCGTACGTA... 

        Rules:

        - Do not output descriptions, notes, or metadata.
        - Do not include non-DNA characters or whitespace.
        - Do not wrap, punctuate, or label the sequence.
        - The sequence length should typically range from 100–500 base pairs, unless otherwise specified.

        Goal: Produce the most plausible starting DNA sequence corresponding to the biological description, optimized for interpretability and compatibility with Evo 2.
        ''',
        key="system_prompt"
    )
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

st.title("Vitro")
st.caption("As of now, there are a variety of machine learning methods to create DNA. However, they all require DNA primers as input. This model allows for a DNA primer to be generated from natural language.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Describe a cell/organism."}]

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

    # send the system prompt first, then the chat messages from the session to the API
    messages_for_api = [{"role": "system", "content": system_prompt}] + st.session_state.messages

    response = client.chat.completions.create(
        model="ft:gpt-4.1-nano-2025-04-14:personal:nucleotide-primer:CVuPZNqP",
        messages=messages_for_api
    )
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)