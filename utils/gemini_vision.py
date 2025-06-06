import google.generativeai as genai
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def call_gemini_vision(image_path, prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    img_b64 = encode_image(image_path)
    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/jpeg",
                "data": img_b64
            }
        ]
    )
    return response.text  # Gemini返回的文本内容 