#!/usr/bin/env python3
import streamlit as st
from transformers import pipeline


def load_tutor():
    # Load a simple language model for demonstration
    return pipeline('text-generation', model='gpt2', max_length=50)


def main():
    st.title('SchoolAI Tutor')
    tutor = load_tutor()
    query = st.text_input('Ask a question:')
    if query:
        response = tutor(query)[0]['generated_text']
        st.write(response)


if __name__ == '__main__':
    main()
