import openai
import base64
import json
from os import environ
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]



def encode_image(image_path):
    """Convert image to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def call_gpt4_vision(image_path, prompt):
    """Call GPT-4 Vision API to analyze image"""
    base64_image = encode_image(image_path)
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Using the official GPT-4 Vision model
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )
        return response
    except Exception as e:
        print(f"Error calling GPT-4 Vision API: {str(e)}")
        raise

def save_json_response(response, output_file="response.json"):
    """Save API response to JSON file"""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=4, ensure_ascii=False)
    print(f"JSON response saved to {output_file}") 
