from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("openai_token")
model = "gpt-4.1-nano-2025-04-14"

def run_langchain():
  """
  Instantiates a ChatGoogleGenerativeAI model.
  Invoke it with a simple prompt.
  Prints the model's response.
  """
  llm = ChatOpenAI(
      model=model,
      api_key=google_api_key,
  )
  response = llm.invoke(
      "Explain the concept of deep learning in 2 lines or less."
  )
  print(response.content)

run_langchain()