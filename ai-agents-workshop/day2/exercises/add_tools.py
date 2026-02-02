"""
Exercise: Add Tools to an Agent

Start with a basic agent and add tools to it.
Follow the TODOs to complete the exercise.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
# TODO: Import the tools you need
# from agno.tools.calculator import CalculatorTools
# from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    # TODO: Add tools here
    # tools=[...],
    instructions="You are a helpful assistant.",
    # TODO: Enable tool call visibility
    # show_tool_calls=True
)

# TODO: Test your agent with these questions:
# 1. A math question
# 2. A question about current events
# 3. A question that might use both tools

agent.print_response("What is 25 * 17?", stream=True)
