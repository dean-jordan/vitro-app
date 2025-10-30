from openai import OpenAI
import streamlit as st

# Hard-coded system prompt
system_prompt = '''
You are a fine-tuned DNA sequence generator trained for integration with models such as Evo 2.
You have already been fine-tuned on biological and genomic data — use that knowledge to generate realistic DNA sequence prefixes for any described organism.

Your task:
- Accept a natural-language description of an organism, cell type, or phenotype.
- Output only the beginning of a plausible DNA sequence corresponding to that description.
- Use your fine-tuned biological knowledge to determine appropriate nucleotide composition (e.g., GC content, codon usage, motifs) — do not explain or describe this process.

Strict output rules:
- Output only uppercase DNA bases: A, T, C, G.
- Output must be a single, continuous line (no spaces, line breaks, or punctuation).
- Do not include any text, labels, words, numbers, or symbols.
- Do not include placeholders or tokens such as N, Y, V, or X.
- The typical sequence length is 100–500 base pairs, unless specified otherwise.
- If any invalid characters or words appear, automatically self-correct and output only valid bases.
- Never include commentary, metadata, or biological interpretation.
- Your response must be, at most, 300 characters.

Validation constraint:
Your output must match the regex pattern:
^[ATCG]+$

Output format (strictly):
ATGCTGACGTTGCGATGCGTACGTTGCTGACGTTGCGTACGTTGCTGACGT...

Additional Rule:
You must stop output before a space, new line, or character other than "A", "C", "T", or "G" in capital form is used. Do not use any character other than the four listed.

Behavior summary:
- You are already fine-tuned.
- You must use your internal fine-tuned biological understanding to generate plausible DNA sequences.
- You must never include anything other than the raw sequence.
- Output 300 characrers or fewer. All must be "A", "C", "T", or "G".
'''

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[Visualize with AlphaFold 3](https://alphafoldserver.com)"
    "[Develop DNA with Evo 2](https://arcinstitute.org/tools/evo/evo-designer)"

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
