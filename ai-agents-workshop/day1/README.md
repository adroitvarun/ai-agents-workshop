# Day 1: Foundations

## What Are LLMs and Why Do They Need Tools?

Welcome to Day 1! Today we'll understand what Large Language Models (LLMs) really are and why they need tools to be truly useful.

---

## What is an LLM?

Think of an LLM as **sophisticated autocomplete** trained on internet text.

When you type "The capital of France is", an LLM predicts the most likely next word based on patterns it learned during training. It's not "looking up" the answer—it's pattern matching.

**Key insight**: LLMs don't "know" things in the way humans do. They've learned statistical patterns from text and generate plausible responses.

---

## The Three Big Limitations

### 1. Frozen Knowledge
LLMs have a **knowledge cutoff date**. They don't know anything that happened after their training ended.

Ask about yesterday's news? They can't help.

### 2. Unreliable Math
LLMs are language models, not calculators. They often make mistakes with:
- Multi-step calculations
- Large numbers
- Precise arithmetic

They'll confidently give you wrong answers!

### 3. Can't Take Actions
LLMs can only generate text. They cannot:
- Send emails
- Search the web
- Access files
- Interact with the real world

---

## Enter: Tool Calling

**Tool calling** is how we extend LLM capabilities. Here's how it works:

1. You give the LLM a list of available tools (with descriptions)
2. You ask a question
3. The LLM decides if a tool would help
4. If yes, it *requests* the tool be used (with parameters)
5. The framework *executes* the tool
6. Results go back to the LLM
7. The LLM generates a final response

```
User: "What's 847 * 293?"
  ↓
LLM thinks: "I should use the calculator tool"
  ↓
LLM outputs: {tool: "calculator", operation: "multiply", a: 847, b: 293}
  ↓
Framework executes calculator → 248071
  ↓
LLM receives result → "847 * 293 = 248,071"
```

**Important**: The LLM doesn't run the tool—it just asks for it. The agent framework handles execution.

---

## What We'll Build Today

1. **Basic Agent** (`01_basic_agent.py`)
   - Create your first agent
   - See it respond to simple queries

2. **Test Limitations** (`02_test_limitations.py`)
   - Try questions that require tools
   - Observe where the agent struggles

3. **Exercise: Explore** (`exercises/explore_agent.py`)
   - Experiment with different prompts
   - Try different instructions

---

## Key Concepts

| Term | Meaning |
|------|---------|
| **LLM** | Large Language Model - the AI that generates text |
| **Agent** | LLM + tools + instructions |
| **Tool** | A function the LLM can request to be executed |
| **Instructions** | System prompt that shapes agent behavior |

---

## Running the Examples

```bash
# Make sure you're in the workshop directory with your .env set up

# Run basic agent
uv run python day1/01_basic_agent.py

# Test limitations
uv run python day1/02_test_limitations.py

# Try the exercise
uv run python day1/exercises/explore_agent.py
```

---

## Next Up

Tomorrow, we'll add tools to fix these limitations! You'll see the same questions get correct answers once we add calculator and web search tools.
