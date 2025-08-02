import os
import requests
import PyPDF2
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("openai_token")
model = "o4-mini"

client = OpenAI(api_key=api_key)

url = """https://raw.githubusercontent.com/hereandnowai/sathyabama-be-cse-ai-pt1-07-2025-hands-on-professional-training-on-genai-and-ai-agents/main/general-profile-of-hereandnowai.pdf"""
response = requests.get(url)

pdf_path = os.path.join(os.path.dirname(__file__), "profile-of-here-and-now-ai.pdf")

with open(pdf_path, "wb") as pdf_file:
    pdf_file.write(response.content)

try:
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        pdf_text_chunks = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text_chunks.append(page_text)
        pdf_context = (
            "\n".join(pdf_text_chunks) if pdf_text_chunks else "No text found in PDF."
        )
except Exception as e:
    print(f"Error reading PDF file: {e}")
    pdf_context = "Error reading PDF file."


def get_response(message, history):
    messages = [
        {
            "role": "system",
            "content": f"""You are Caramel AI, built by Here and Now AI.
                 Respond to the user's queries **only** with information from {pdf_context}.""",
        }
    ]
    messages.extend(history)
    messages.append({"role": "user", "content": message})
    response = (
        client.chat.completions.create(model=model, messages=messages)
        .choices[0]
        .message.content
    )
    return response