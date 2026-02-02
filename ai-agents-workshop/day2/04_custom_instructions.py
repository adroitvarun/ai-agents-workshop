"""
Day 2: The Art of Instructions

Same tools, different instructions = different behavior!
Run this to see how instructions shape the agent.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

tools = [CalculatorTools(), DuckDuckGoTools()]
question = "What's 15% of $127.50 for a tip?"

# Style 1: Concise Expert
print("=" * 50)
print("STYLE 1: Concise Expert")
print("=" * 50)
agent1 = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="Be extremely brief. Answer in one sentence maximum.",
    show_tool_calls=True
)
agent1.print_response(question, stream=True)

# Style 2: Friendly Teacher
print("\n" + "=" * 50)
print("STYLE 2: Friendly Teacher")
print("=" * 50)
agent2 = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="Explain like I'm learning. Break down the steps simply.",
    show_tool_calls=True
)
agent2.print_response(question, stream=True)

# Style 3: Formal Accountant
print("\n" + "=" * 50)
print("STYLE 3: Formal Accountant")
print("=" * 50)
agent3 = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="You are a professional accountant. Be precise and formal. Always show your calculations.",
    show_tool_calls=True
)
agent3.print_response(question, stream=True)
