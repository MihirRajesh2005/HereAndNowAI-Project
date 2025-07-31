from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"

def run_langchain():
  """
  Instantiates a ChatGoogleGenerativeAI model.
  Invoke it with a simple prompt.
  Prints the model's response.
  """
  llm = ChatGoogleGenerativeAI(
      model=model,
      api_key=google_api_key,
  )
  response = llm.invoke(
      "Explain the concept of deep learning in 2 lines or less."
  )
  print(response.content)

run_langchain()