"""
Exercise: Explore the Basic Agent

Try different prompts and observe the agent's behavior.
Fill in the TODOs below.

Tasks:
1. Ask questions that require current information
2. Ask complex math problems
3. Try different instructions and see how behavior changes
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# TODO: Modify the instructions to give the agent a personality
# Examples: "You are a pirate", "You are a formal British butler", "You speak only in haiku"
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are a helpful assistant."  # <-- MODIFY THIS
)

# TODO: Try at least 3 different prompts
# Observe: What can the agent do well? What does it struggle with?

# Prompt 1: Ask about something current
agent.print_response("YOUR PROMPT HERE", stream=True)

# Prompt 2: Ask a math question
# agent.print_response("YOUR PROMPT HERE", stream=True)

# Prompt 3: Ask it to do something in the real world
# agent.print_response("YOUR PROMPT HERE", stream=True)
