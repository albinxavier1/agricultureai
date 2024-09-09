import os
from groq import Groq
import streamlit as st

# Streamlit app title
st.title("Agriculture Assistant")

# Input prompt from user
prompt = st.text_input("Enter the prompt:")

if st.button("Get Response"):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Act as a helpful assistant who specializes in agriculture and farming. Explain the {prompt} on the given context of agriculture and farmer and guide them as an assistant",
            }
        ],
        model="llama3-70b-8192",
    )

    # Display the response
    st.write(chat_completion.choices[0].message.content)