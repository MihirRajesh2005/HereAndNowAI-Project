from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("openai_token")
model = "o4-mini"

def run_langchain():
  """
  Instantiates a ChatGoogleGenerativeAI model.
  Invoke it with a simple prompt.
  Prints the model's response.
  """
  llm = ChatOpenAI(
      model=model,
      api_key=api_key,
  )
  response = llm.invoke(
      "Explain the concept of deep learning in 2 lines or less."
  )
  print(response.content)

run_langchain()