from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

ddg = DuckDuckGoSearchRun()

@tool
def search(query: str) -> str:
    """Search the web for current information."""
    return ddg.invoke(query)