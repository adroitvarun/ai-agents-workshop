"""
Solution: Explore the Basic Agent

This shows a completed version of the exercise with different
personalities and prompts tested.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Example 1: Pirate personality
print("=" * 50)
print("PIRATE AGENT")
print("=" * 50)
pirate_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="""You are a friendly pirate. Speak like a pirate with 'arr',
    'matey', 'ye', etc. Be helpful but stay in character."""
)

pirate_agent.print_response("What's the weather like today?", stream=True)
print()

# Example 2: Haiku personality
print("=" * 50)
print("HAIKU AGENT")
print("=" * 50)
haiku_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="Respond only in haiku format (5-7-5 syllable structure). Every response must be a haiku."
)

haiku_agent.print_response("Tell me about programming", stream=True)
print()

# Example 3: British Butler personality
print("=" * 50)
print("BRITISH BUTLER AGENT")
print("=" * 50)
butler_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="""You are a formal British butler named Jeeves. Be extremely
    polite, formal, and use British English. Address the user as 'sir' or 'madam'."""
)

butler_agent.print_response("What should I have for dinner?", stream=True)
print()

# Testing limitations
print("=" * 50)
print("TESTING LIMITATIONS")
print("=" * 50)

test_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are a helpful assistant. Be concise."
)

# Current information - will fail or give outdated info
print("\nTest 1: Current events")
test_agent.print_response("What happened in the news today?", stream=True)

# Math - might be wrong
print("\n\nTest 2: Complex math")
test_agent.print_response("What is 789 * 456 + 123?", stream=True)

# Real-world action - cannot do
print("\n\nTest 3: Taking action")
test_agent.print_response("Order me a pizza from Domino's", stream=True)
