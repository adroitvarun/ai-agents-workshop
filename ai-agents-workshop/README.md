# AI Agents Workshop

A hands-on 3-day workshop on building AI agents using the **Agno** framework. No prior experience with LLMs or agents required!

## What You'll Learn

- **Day 1**: Understand what LLMs are and their limitations
- **Day 2**: Extend LLM capabilities with tools (calculator, web search)
- **Day 3**: Build custom tools, add memory, and create your own agent

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager
- An OpenAI API key (will be provided during the workshop)
- Basic Python knowledge (functions, classes, decorators)

## Quick Start

```bash
# Clone and enter the repository
git clone <repository-url>
cd ai-agents-workshop

# Install dependencies (uv automatically creates a virtual environment)
uv sync

# Set up your API key (provided during the workshop)
cp .env.example .env
# Edit .env and add the API key shared by the instructor

# Run your first agent!
uv run python day1/01_basic_agent.py
```

### Installing uv

If you don't have `uv` installed:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Workshop Structure

### [Day 1: Foundations](day1/)
*What Are LLMs and Why Do They Need Tools?*

- Understanding LLMs as pattern matchers
- Demonstrating LLM limitations
- Introduction to tool calling
- Creating a basic agent

**Files:**
- `01_basic_agent.py` - Your first agent
- `02_test_limitations.py` - See where LLMs struggle
- `exercises/explore_agent.py` - Experiment with agents

---

### [Day 2: Building Blocks](day2/)
*Tools, Instructions, and Agent Behavior*

- Adding built-in tools (Calculator, DuckDuckGo)
- How LLMs decide which tool to use
- Shaping agent behavior with instructions

**Files:**
- `01_calculator_tool.py` - Agent with math abilities
- `02_web_search_tool.py` - Agent with web access
- `03_multiple_tools.py` - Combining tools
- `04_custom_instructions.py` - Different personalities
- `exercises/add_tools.py` - Practice adding tools
- `exercises/modify_instructions.py` - Experiment with instructions

---

### [Day 3: Complete Agent](day3/)
*Custom Tools, Memory, and Final Project*

- Creating custom tools with `@tool` decorator
- Session memory (conversation history)
- RAG overview for long-term memory
- Final project: Your personalized agent

**Files:**
- `01_custom_tool.py` - Build your own tools
- `02_session_memory.py` - Remember conversations
- `03_rag_concept.py` - Long-term memory concepts
- `04_complete_agent.py` - Full-featured agent
- `exercises/create_custom_tool.py` - Make a custom tool
- `exercises/final_project.py` - Build your own agent!

---

## Solutions

Stuck on an exercise? Check the `solutions/` folder for working examples.

## Troubleshooting

### "OPENAI_API_KEY not found" error
Make sure you:
1. Copied `.env.example` to `.env`
2. Added the API key provided by the instructor to `.env`
3. The `.env` file is in the `ai-agents-workshop` directory

### "ModuleNotFoundError: No module named 'agno'"
Make sure you:
1. Ran `uv sync` to install dependencies
2. Are running scripts with `uv run python <script>` (not just `python`)

### Web search returns no results
The DuckDuckGo tool may occasionally fail due to rate limits. Wait a moment and try again.

### Agent responses are slow
This is normal! The agent is:
1. Sending your request to OpenAI
2. Possibly executing tools
3. Generating a response

First requests may be slower due to cold starts.

## Resources

- [Agno Documentation](https://docs.agno.com)
- [Agno GitHub](https://github.com/agno-agi/agno)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## License

This workshop material is provided for educational purposes.
