# Day 3: Complete Agent

## Custom Tools, Memory, and Final Project

Today we bring it all together! You'll create custom tools, add conversation memory, and build your own personalized agent.

---

## Creating Custom Tools

Any Python function can become a tool! The magic ingredients:

1. **`@tool` decorator** - Marks the function as a tool
2. **Type hints** - Help the LLM understand parameters
3. **Docstring** - Becomes the tool description (LLM reads this!)

### Basic Pattern:
```python
from agno.tools import tool

@tool
def my_tool(param1: str, param2: int = 10) -> str:
    """Short description of what the tool does.

    Args:
        param1: Description of this parameter
        param2: Description with default value

    Returns:
        What the tool returns
    """
    # Your code here
    return "result"
```

### Why Docstrings Matter

The LLM reads your docstring to decide when to use the tool!

```python
# Bad - LLM doesn't know when to use this
@tool
def do_thing(x):
    return x * 2

# Good - LLM understands this doubles numbers
@tool
def double_number(number: int) -> int:
    """Double a number. Use this when asked to multiply by 2."""
    return number * 2
```

---

## Session Memory

By default, each agent call is independent. Add `AgentMemory` to remember conversations:

```python
from agno.memory import AgentMemory

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    memory=AgentMemory()  # Enables conversation memory
)

# Now the agent remembers previous messages
agent.print_response("My name is Alex")
agent.print_response("What's my name?")  # It remembers!
```

### How It Works
1. Each message (user + assistant) is stored
2. The entire conversation is sent with each new request
3. The LLM sees full history and can reference it

### Limitation
Memory only lasts for the current session. Restart the script = memory gone.

---

## RAG: Long-Term Memory (Conceptual)

**RAG** (Retrieval-Augmented Generation) lets agents access large documents:

1. **Setup**: Documents are split into chunks and stored with "embeddings"
2. **Query**: When you ask a question, relevant chunks are retrieved
3. **Answer**: The LLM answers based on the retrieved content

This enables:
- Chatting with your documents
- Agents that know your company's knowledge base
- Persistent memory across sessions

We won't implement RAG today, but see `03_rag_concept.py` for an overview.

---

## Today's Files

1. **`01_custom_tool.py`** - Create dice roller, coin flip, and random number tools
2. **`02_session_memory.py`** - Agent that remembers your conversation
3. **`03_rag_concept.py`** - Conceptual overview of RAG (no setup needed)
4. **`04_complete_agent.py`** - Full agent with tools + memory + interactive loop

### Exercises:
- **`exercises/create_custom_tool.py`** - Build your own custom tool
- **`exercises/final_project.py`** - Create your personalized agent!

---

## Running the Examples

```bash
# Custom tools
uv run python day3/01_custom_tool.py

# Session memory
uv run python day3/02_session_memory.py

# RAG concepts (just prints explanation)
uv run python day3/03_rag_concept.py

# Complete agent (interactive!)
uv run python day3/04_complete_agent.py
```

---

## Final Project Requirements

Build an agent with:

- [ ] At least 2 built-in tools (calculator, web search, etc.)
- [ ] At least 1 custom tool you create
- [ ] Session memory enabled
- [ ] Custom instructions that give your agent a personality

### Ideas:
| Agent | Tools | Personality |
|-------|-------|-------------|
| D&D Game Master | dice, web search | Dramatic storyteller |
| Research Assistant | web search, notes | Academic and thorough |
| Trivia Host | random, web search | Energetic game show host |
| Finance Helper | calculator, web search | Professional advisor |

---

## Key Takeaways

1. **Any function can be a tool** with `@tool` decorator
2. **Docstrings are crucial** - they help the LLM choose tools
3. **Session memory** keeps conversation context
4. **RAG** enables long-term knowledge (future learning)

---

## What's Next?

Congratulations on completing the workshop! Next steps:

1. **Explore Agno's cookbook** - More advanced examples
2. **Try RAG** - Add document knowledge to your agents
3. **Build something real** - Apply what you've learned!

Resources:
- [Agno Documentation](https://docs.agno.com)
- [Agno Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
