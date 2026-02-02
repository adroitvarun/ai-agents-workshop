"""
Solution: Experiment with Instructions

Three agents with unique personalities, same tools.
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools

tools = [CalculatorTools(), DuckDuckGoTools()]
test_question = "What's the population of Japan and what's that divided by 47 prefectures?"

# Agent 1: Pirate
print("=" * 50)
print("AGENT 1: PIRATE")
print("=" * 50)
pirate_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="""You are a pirate who loves finding treasure (information).
    Speak like a pirate with 'arr', 'matey', 'ye scallywag', etc.
    When you search the web, you're 'searching the seven seas'.
    When you calculate, you're 'counting yer doubloons'.
    Stay in character but be helpful!""",
    show_tool_calls=True
)
pirate_agent.print_response(test_question, stream=True)

# Agent 2: Strict Math Teacher
print("\n" + "=" * 50)
print("AGENT 2: STRICT MATH TEACHER")
print("=" * 50)
teacher_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="""You are a strict but fair math teacher named Professor Smith.
    Always show your work step by step.
    Explain the reasoning behind each calculation.
    Use proper mathematical notation when possible.
    End with a summary of what we learned.""",
    show_tool_calls=True
)
teacher_agent.print_response(test_question, stream=True)

# Agent 3: News Anchor
print("\n" + "=" * 50)
print("AGENT 3: NEWS ANCHOR")
print("=" * 50)
anchor_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=tools,
    instructions="""You are a professional news anchor delivering a report.
    Start with 'Good evening, I'm bringing you the latest...'
    Present information formally and authoritatively.
    Cite your sources.
    End with 'Back to you in the studio.' or similar.""",
    show_tool_calls=True
)
anchor_agent.print_response(test_question, stream=True)
