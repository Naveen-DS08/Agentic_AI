from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo 

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Creating our agent for web search
websearch_agent = Agent(
    name = "AI Web Search Agent",
    role = "Search the web to extract the information",
    model = Groq(id="llama3-70b-8192"),
    tools = [DuckDuckGo()],
    instructions = ["Always provide me the source"],
    show_tool_calls= True,
    markdown= True
    )

# Creat our Financial Agent
financial_agent = Agent(
    name = "Financial AI Agent",
    role = "Extract the entire information about the stocks",
    model= Groq(id = "llama3-70b-8192"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, 
                           stock_fundamentals= True, company_news= True,
                           company_info=True)],
    instructions= ["Use tables to display the data"],
    show_tool_calls= True,
    markdown = True
    )

# Combining these agents into a team 
multi_ai_agent = Agent(
    team= [websearch_agent, financial_agent],
    model = Groq(id = "llama3-70b-8192"),
    instructions= ["Provide me the source", "Use tables to display the data"],
    show_tool_calls= True, 
    markdown = True
    )

# Initiate the agent
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)
