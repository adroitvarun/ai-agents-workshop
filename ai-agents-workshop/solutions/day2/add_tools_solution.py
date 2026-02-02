"""
Solution: Add Tools to an Agent

This shows the completed exercise with tools properly added.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Create agent with both tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools(), DuckDuckGoTools()],
    instructions="""You are a helpful assistant with access to a calculator
    and web search. Use the calculator for any math, and web search for
    current information.""",
    show_tool_calls=True
)

# Test 1: Math question (should use calculator)
print("=" * 50)
print("Test 1: Math question")
print("=" * 50)
agent.print_response("What is 25 * 17?", stream=True)

# Test 2: Current events (should use web search)
print("\n" + "=" * 50)
print("Test 2: Current events")
print("=" * 50)
agent.print_response("What's the latest news about AI?", stream=True)

# Test 3: Combined question (might use both)
print("\n" + "=" * 50)
print("Test 3: Combined question")
print("=" * 50)
agent.print_response(
    "What's the current US population and what's 10% of that?",
    stream=True
)

# Test 4: Another math question
print("\n" + "=" * 50)
print("Test 4: Percentage calculation")
print("=" * 50)
agent.print_response(
    "If a shirt costs $45 and is 30% off, what's the final price?",
    stream=True
)
