from openai import OpenAI
from dotenv import load_dotenv
import os
from prompts import ai_motivational_speaker

load_dotenv()
api_key = os.getenv("openai_token")
model = "o4-mini"

client = OpenAI(api_key=api_key)
ai_motivational_speaker = ai_motivational_speaker


def get_response(message, history):
    messages = [{"role": "system", "content": ai_motivational_speaker}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})
    response = client.chat.completions.create(model=model, messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response