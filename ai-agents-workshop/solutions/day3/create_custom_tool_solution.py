"""
Solution: Create Your Own Custom Tool

This shows several example custom tools you could create.
"""

from dotenv import load_dotenv
load_dotenv()

import random
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool

# Example 1: Temperature Converter
@tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value: The temperature value to convert
        from_unit: The unit to convert from ('C', 'F', or 'K')
        to_unit: The unit to convert to ('C', 'F', or 'K')

    Returns:
        The converted temperature with units
    """
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert to Celsius first
    if from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        celsius = value

    # Convert from Celsius to target
    if to_unit == 'F':
        result = celsius * 9/5 + 32
    elif to_unit == 'K':
        result = celsius + 273.15
    else:
        result = celsius

    return f"{value}{from_unit} = {result:.2f}{to_unit}"


# Example 2: Magic 8-Ball
@tool
def magic_8_ball(question: str) -> str:
    """Ask the Magic 8-Ball a yes/no question and get a mystical answer.

    Args:
        question: The yes/no question to ask

    Returns:
        A mystical answer from the Magic 8-Ball
    """
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    return f"The Magic 8-Ball says: {random.choice(answers)}"


# Example 3: Unit Converter (Distance)
@tool
def convert_distance(value: float, from_unit: str, to_unit: str) -> str:
    """Convert distance between miles, kilometers, meters, and feet.

    Args:
        value: The distance value to convert
        from_unit: The unit to convert from ('miles', 'km', 'm', 'feet')
        to_unit: The unit to convert to ('miles', 'km', 'm', 'feet')

    Returns:
        The converted distance with units
    """
    # Convert everything to meters first
    to_meters = {
        'miles': 1609.34,
        'km': 1000,
        'm': 1,
        'feet': 0.3048
    }

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in to_meters or to_unit not in to_meters:
        return "Unknown unit. Use 'miles', 'km', 'm', or 'feet'."

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]

    return f"{value} {from_unit} = {result:.4f} {to_unit}"


# Create agent with all custom tools
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[convert_temperature, magic_8_ball, convert_distance],
    instructions="""You are a helpful assistant with these special abilities:
    - Convert temperatures between Celsius, Fahrenheit, and Kelvin
    - Answer yes/no questions with the Magic 8-Ball
    - Convert distances between miles, km, meters, and feet

    Use these tools when the user asks relevant questions.""",
    show_tool_calls=True
)

# Test the tools
print("=" * 50)
print("Testing Custom Tools")
print("=" * 50)

print("\nTemperature conversion:")
agent.print_response("What is 100 degrees Fahrenheit in Celsius?", stream=True)

print("\n\nMagic 8-Ball:")
agent.print_response("Will I learn a lot in this workshop?", stream=True)

print("\n\nDistance conversion:")
agent.print_response("How many kilometers is a marathon (26.2 miles)?", stream=True)
