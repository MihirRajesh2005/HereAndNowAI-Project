from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
import os
import ast

load_dotenv()
google_api_key = os.getenv("openai_token")
model = "o3-mini-2025-01-31"

@tool
def web_scrap(urls: str) -> str:
    """
    Scrap content from a list of URLs.
    The input should be a string representation of a pythonl list of URLs.
    (e.g., "['https://hereandnowai.com', 'https://sathyabama.ac.in']")
    Returns the concatenated text content of all the scrapped pages.
    """
    try:
        url_list=ast.literal_eval(urls)
        if not isinstance(url_list, list) or not all(isinstance(url,str) for url in url_list):
            return "Invalid input"
    except (ValueError, SyntaxError):
        return "Invalid input format. Please provide a list of URLs as a string."
    combined_content = []
    for url in url_list:
        try:
            loader = WebBaseLoader(
                [url], requests_kwargs = {"headers": {"User-Agent": "Caramel AI"}}
            )
            data = loader.load()
            for doc in data:
              combined_content.append(doc.page_content)
        except Exception as e:
            combined_content.append(f"Could not scrape {url}. Error: {e}")
    
    return "\n\n".join(combined_content)

def ai_agent():
    """
    Creates and runs an agent that can use the web_scrap tool.
    """
    llm = ChatOpenAI(model=model, api_key=google_api_key)
    tool  = [web_scrap]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tool, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool, 
                                   verbose=False, handle_parsing_errors=True)
    question = "What is the story of Here and Now AI? The url is https://hereandnowai.com"
    response = agent_executor.invoke({"input":question})
    print(f"Response: {response['output']}")

ai_agent()