from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("openai_token")
model = "o4-mini"
client = OpenAI(api_key=api_key)
url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
response = requests.get(url)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "profile-of-hereandnowai.txt")

with open(file_path, "wb") as file:
    file.write(response.content)

text_path = file_path

try:
    with open(text_path, "r", encoding="utf-8") as file:
        text_lines = file.readlines()
        text_context = "\n".join(line.strip() for line in text_lines if line.strip())
except Exception as e:
    print(f"Error reading file: {e}")
    text_context = "Error extracting text from text file."


def get_response(message, history):
    system_prompt = f"""You are Caramel AI, an assistant built by Here and Now AI.
    **Answer the user's question based only on the following context:\n\n{text_context}**"""
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})
    response = (
        client.chat.completions.create(model=model, messages=messages)
        .choices[0]
        .message.content
    )
    return response
