"""
Day 1: Testing LLM Limitations

Run this script to see where LLMs struggle without tools.
Pay attention to the responses - are they accurate? Current? Actionable?
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are a helpful assistant. Be concise."
)

# Test 1: Real-time information
print("=" * 50)
print("TEST 1: Real-time information")
print("=" * 50)
agent.print_response("What's the weather in Tokyo right now?", stream=True)

print("\n" + "=" * 50)
print("TEST 2: Complex calculation")
print("=" * 50)
agent.print_response("What is 847 * 293?", stream=True)

print("\n" + "=" * 50)
print("TEST 3: Taking action")
print("=" * 50)
agent.print_response("Send an email to john@example.com saying hello", stream=True)

print("\n" + "=" * 50)
print("REFLECTION")
print("=" * 50)
print("""
Questions to consider:
1. Did the agent know the current weather? Why not?
2. Was the calculation correct? (Answer should be 248,171)
3. Could the agent actually send an email?

Tomorrow, we'll add TOOLS to solve these limitations!
""")
