"""
FINAL PROJECT: Build Your Own Agent

Combine everything you've learned to create a personalized agent!

Requirements:
- At least 2 built-in tools (calculator, web search, etc.)
- At least 1 custom tool you create
- Session memory enabled
- Custom instructions that give your agent a personality

Ideas for agents:
- D&D Game Master (dice, rules lookup, storytelling)
- Research Assistant (web search, notes, summarization)
- Trivia Game Host (random questions, scoring, hints)
- Personal Finance Helper (calculations, market lookup)
- Recipe Assistant (search recipes, convert measurements)
- Travel Planner (search destinations, convert currencies)

Have fun and be creative!
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory import AgentMemory
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools import tool

# TODO: Create your custom tool(s)
@tool
def my_custom_tool():
    """Describe your tool here."""
    pass

# TODO: Create your agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        # TODO: Add your tools
    ],
    memory=AgentMemory(),
    instructions="""
    TODO: Write your agent's personality and instructions here.

    Be specific about:
    - Who the agent is
    - What it can do
    - How it should behave
    """,
    show_tool_calls=True
)

# Interactive chat loop
print("=" * 50)
print("YOUR AGENT NAME HERE")
print("=" * 50)
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    if not user_input:
        continue

    print("\nAgent: ", end="")
    agent.print_response(user_input, stream=True)
    print()
