LangChain Tool-Using Agent

This project demonstrates a LangChain-based AI agent capable of dynamically selecting and using tools to answer user queries. The agent can call external APIs and reason over queries using a Groq LLM.

Features

Tool-based agent using LangChain

DuckDuckGo search integration

Weather API integration (Weatherstack)

Groq LLM (LLaMA 3.1)

How it works

User asks a question

Agent internally decides which tool to use

The selected tool executes

Agent returns the final response

Setup

Install dependencies
pip install -r requirements.txt

Create a .env file with your API keys:
GROQ_API_KEY=your_groq_key
WEATHERSTACK_API_KEY=your_weatherstack_key

Run the script
python Agents_langchain.py

Example
User: What is the weather in Hyderabad?
Agent: The weather in Hyderabad is Sunny with temperature 32°C

Notes
This project focuses on creating a simple, tool-using agent with LangChain. Future enhancements can include multi-agent systems, advanced reasoning pipelines, and integration with LangGraph for stateful workflows.