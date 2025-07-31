from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

google_api_key = os.getenv("openai_token")
model = "gpt-4.1-nano-2025-04-14"

def simple_chatbot():
  """
  continuously prompts the user for input
  feeds it to the llm and prints the response
  exits when the user types 'quit'
  """
  llm = ChatOpenAI(
    api_key = google_api_key,
    model = model
  )
  while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
      print("Exiting the chatbot. Goodbye!")
      break
    response = llm.invoke(user_input)
    print(f"Bot: {response.content}")

simple_chatbot()