import streamlit as st
from langchain_community.llms import Ollama

prompt_input = st.text_input("Prompt")
button = st.button("GO")

if button and prompt_input != "":
  llm_model = Ollama(model="qwen2.5")

  response = llm_model.invoke(prompt_input)

  st.markdown(response)

