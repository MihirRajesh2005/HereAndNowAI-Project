from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_core.rate_limiters import InMemoryRateLimiter
import os

load_dotenv()
api_key = os.getenv("openai_token")
model = "o3-mini-2025-01-31"

facts = {
  "capital of france": "Paris",
  "largest planet": "Jupiter",
  "largest ocean": "Pacific Ocean",
  "first president of the USA": "George Washington",
}

@tool
def get_fact(query: str) -> str:
  """
  Retreives facts from a predefined list. Query must be an exact match.
  """
  return facts.get(query.lower(), "Fact not found.")

def data_retreival():
  """
  creates an agent that uses the get_fact tool.
  """
  rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.2, 
    check_every_n_seconds=0.5, 
    max_bucket_size=3
  )
  llm = ChatOpenAI(model=model, 
                   api_key=api_key, 
                   request_timeout=120, 
                   rate_limiter=rate_limiter)
  tool = [get_fact]
  prompt = hub.pull("hwchase17/react")
  agent = create_react_agent(llm, tool, prompt=prompt)
  agent_executor = AgentExecutor(agent=agent, 
                                 tools=tool, 
                                 verbose = False, 
                                 handle_parsing_errors=True)
  responses = []
  print("\n---Query 1: Capital of France---")
  responses.append(agent_executor.invoke({"input": "What is the capital of France?"}))

  print("---Query 2: Largest Planet---")
  responses.append(agent_executor.invoke({"input": "What is the largest planet?"}))

  print("---Query 3: Largest Ocean---")
  responses.append(agent_executor.invoke({"input": "What is the largest ocean?"}))

  print("---Query 4: First President of the USA---")
  responses.append(agent_executor.invoke({"input": "Who was the first president of the USA?"}))

  print("\n---Responses---")
  for i, response in enumerate(responses, start=1):
    print(f"Response {i}: {response['output']}")

data_retreival()