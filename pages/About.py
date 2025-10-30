from openai import OpenAI
import streamlit as st

with st.sidebar:
    "[Visualize with AlphaFold 3](https://alphafoldserver.com)"
    "[Develop DNA with Evo 2](https://arcinstitute.org/tools/evo/evo-designer)"

st.title("Information")
st.caption("About the App")

st.header("Synthetic DNA Engineering with Vitro")

st.text("Vitro is a tool for creating DNA prefixes. DNA prefixes are extremely useful in a variety of fields, including synthetic biology and chemistry, as they are the input for machine learning models such as Evo 2. These models can generate entire genomes from these prefixes, hence allowing for synthetic life to be generated. By creating more complex prefixes, more complex life can be synthetically generated. Hence, Vitro exists as a tool to create complex life through prefix development.")

st.header("AlphaFold 2/AlphaFold 3 Integration")

st.text("To visualize generated prefixes or full sequences (generated with Evo 2 and Vitro) on AlphaFold 3, simply use the link on the sidebar to reach the AlphaFold Server. The AlphaFold Server is a cloud-based platform for visualizing proteins, DNA, and RNA sequences. Note that a standard account is limited to 30 visualizations per day, however this quota is sufficient for Vitro. Note that Vitro contains full compatibility with AlphaFold 2 as it was trained on the NCBI GenBank dataset, allowing for full biological plausibility.")

st.header("Use of Prefixes for Evo/Evo 2")

st.text("One of the most crucial applications for a generated prefix is creating a full DNA sequence. This can be done with Evo 2. The link in the sidebar directs to the Evo 2 Server, which can be used to add nucleotides to the prefixes to create novel life. As Vitro is trained on NCBI GenBank's annotated genomes, an accuracy of ~92 percent is observed, hence being highly accurate. This means that Vitro contains full compatibility with Evo 2 alongside AlphaFold. Note that generated sequences may not be fully optimized. However, Evo 2/Vitro sequences will be fully biologically plausible.")