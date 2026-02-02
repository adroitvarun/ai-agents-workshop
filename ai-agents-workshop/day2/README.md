# Day 2: Building Blocks

## Tools, Instructions, and Agent Behavior

Yesterday you saw LLM limitations. Today we fix them with tools!

---

## How Tools Extend LLM Capabilities

Tools are functions that the LLM can request to execute. The agent framework:
1. Tells the LLM what tools are available (name, description, parameters)
2. The LLM decides when to use them
3. The framework executes the tool and returns results
4. The LLM incorporates results into its response

---

## Built-in Tools in Agno

### CalculatorTools
Gives the agent accurate math abilities:
```python
from agno.tools.calculator import CalculatorTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools()]
)
```

### DuckDuckGoTools
Gives the agent web search capabilities:
```python
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()]
)
```

---

## How LLMs Decide Which Tool to Use

The LLM reads tool descriptions and decides based on:
1. **The user's question** - What are they asking for?
2. **Tool descriptions** - Which tool seems relevant?
3. **Instructions** - Any guidance on tool usage?

The LLM doesn't always make perfect decisions! Good tool descriptions and instructions help.

---

## Debugging with `show_tool_calls=True`

Enable this to see when tools are used:
```python
agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[CalculatorTools()],
    show_tool_calls=True  # Shows tool usage in output
)
```

You'll see output like:
```
[Tool: calculator] multiply(847, 293) -> 248071
```

This is invaluable for understanding agent behavior!

---

## The Power of Instructions

Instructions shape how the agent:
- **Communicates** (formal vs casual, brief vs detailed)
- **Uses tools** (when to search vs when to use existing knowledge)
- **Handles edge cases** (what to do when uncertain)

Same tools + different instructions = different behavior!

### Examples:
```python
# Concise expert
instructions = "Be brief. One sentence max."

# Friendly teacher
instructions = "Explain like I'm learning. Break down steps."

# Professional accountant
instructions = "Be formal and precise. Always show calculations."
```

---

## Today's Files

1. **`01_calculator_tool.py`** - Agent with math abilities
2. **`02_web_search_tool.py`** - Agent with web access
3. **`03_multiple_tools.py`** - Agent that chooses between tools
4. **`04_custom_instructions.py`** - Same tools, different behaviors

### Exercises:
- **`exercises/add_tools.py`** - Practice adding tools to an agent
- **`exercises/modify_instructions.py`** - Experiment with instructions

---

## Running the Examples

```bash
# Calculator tool
uv run python day2/01_calculator_tool.py

# Web search tool
uv run python day2/02_web_search_tool.py

# Multiple tools
uv run python day2/03_multiple_tools.py

# Custom instructions
uv run python day2/04_custom_instructions.py
```

---

## Key Takeaways

1. **Tools extend LLM capabilities** beyond text generation
2. **The LLM chooses** which tool to use based on the question
3. **`show_tool_calls=True`** lets you see tool usage
4. **Instructions matter** - they shape behavior significantly

---

## Next Up

Tomorrow, we'll create our own custom tools and add memory so the agent remembers your conversation!
