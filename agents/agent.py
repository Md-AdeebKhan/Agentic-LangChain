import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools.search_tool import search
from tools.weather_tool import get_weather

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    api_key=groq_api_key,
    temperature=0
)

tools = [search, get_weather]

system_prompt = """
You are an intelligent AI assistant.

Use tools when needed:
- Use search tool for current information.
- Use weather tool for weather questions.
- Always return a clear and concise answer.
"""

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)