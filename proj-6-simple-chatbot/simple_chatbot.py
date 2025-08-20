from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("openai_token")
model = "o4-mini"

def simple_chatbot():
  """
  continuously prompts the user for input
  feeds it to the llm and prints the response
  exits when the user types 'quit'
  """
  llm = ChatOpenAI(
    api_key = api_key,
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