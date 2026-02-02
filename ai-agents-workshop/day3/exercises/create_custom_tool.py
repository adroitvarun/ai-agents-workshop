"""
Exercise: Create Your Own Custom Tool

Create a custom tool that does something useful or fun!
Follow the pattern and make sure to include a good docstring.

Ideas:
- Temperature converter (Celsius <-> Fahrenheit)
- Unit converter (miles <-> km, etc.)
- Fortune teller / Magic 8-ball
- Joke generator
- Simple todo list manager
- Countdown timer
"""

from dotenv import load_dotenv
load_dotenv()

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool

# TODO: Create your custom tool here
# Remember:
# 1. Use the @tool decorator
# 2. Add type hints for parameters
# 3. Write a clear docstring (this becomes the tool description!)
# 4. Return a string result

@tool
def your_custom_tool():
    """TODO: Describe what your tool does.

    The LLM reads this docstring to understand when to use the tool!
    """
    # TODO: Implement your tool
    pass


# Create an agent with your tool
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[your_custom_tool],  # Add your tool here
    instructions="You are a helpful assistant. Use your tools when appropriate.",
    show_tool_calls=True
)

# TODO: Test your tool with appropriate prompts
agent.print_response("Test your tool here!", stream=True)
