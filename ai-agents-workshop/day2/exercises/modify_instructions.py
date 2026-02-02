"""
Exercise: Experiment with Instructions

Create agents with different personalities/behaviors using only instructions.
The tools stay the same - only the instructions change.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

tools = [CalculatorTools(), DuckDuckGoTools()]

# TODO: Create 3 different agents with unique instruction styles
# Ideas:
# - A pirate who searches for treasure (information)
# - A strict math teacher who always shows work
# - A news anchor who reports search results formally
# - A comedian who makes everything funny

# Agent 1: YOUR STYLE HERE
agent1 = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="TODO: Write your instructions here",
    show_tool_calls=True
)

# Test all agents with the same question
test_question = "What's the population of Japan and what's that divided by 47 prefectures?"

print("Agent 1 Response:")
print("-" * 30)
agent1.print_response(test_question, stream=True)

# TODO: Create and test Agent 2 and Agent 3
