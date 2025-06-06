import openai
import base64
import json
from os import environ
from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]


def call_gpt4_vision(prompt):
    """Call GPT-4 Vision API to analyze image"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Using the official GPT-4 Vision model
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt}
                    ]
                }
            ],
            max_tokens=300
        )
        return response
    except Exception as e:
        print(f"Error calling GPT-4 Vision API: {str(e)}")
        raise
 
if __name__ == "__main__":
    prompt = "who are you?"
    print(call_gpt4_vision(prompt).choices[0].message.content)