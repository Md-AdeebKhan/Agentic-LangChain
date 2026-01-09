from dotenv import load_dotenv
import os
import requests

from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
WEATHERSTACK_API_KEY=os.getenv("WEATHERSTACK_API_KEY")



search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke('top news in india today')

print(results)

@tool
def get_weather(city: str) -> str:
    """Get current weather information for a given city"""
    url = f"https://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}"

    data = requests.get(url).json()

    if "current" not in data:
        return "Weather not found"

    return (
        f"The weather in {city} is "
        f"{data['current']['weather_descriptions'][0]} "
        f"with temperature {data['current']['temperature']}°C"
    )
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

tools = [
    search_tool,
    get_weather
]

agent = create_agent(
    model = llm,
    tools = tools
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in Hyderabad?"}]}
)

print(response["messages"][-1].content)
