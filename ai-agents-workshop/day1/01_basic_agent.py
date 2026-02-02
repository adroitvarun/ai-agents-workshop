"""
Day 1: Your First Agent (No Tools)

This creates a simple agent that can chat but has no external capabilities.
Notice what happens when you ask it questions that require:
- Real-time information
- Complex calculations
- Taking actions
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create a basic agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are a helpful assistant."
)

# Try it out!
agent.print_response("Hello! What can you help me with?", stream=True)
