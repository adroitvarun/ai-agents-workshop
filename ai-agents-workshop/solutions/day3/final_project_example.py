"""
Final Project Example: D&D Game Master

A complete agent that serves as a Dungeons & Dragons game master.
Features:
- Dice rolling for various dice types
- Web search for D&D rules and lore
- Calculator for damage calculations
- Session memory for ongoing adventures
- Rich personality and storytelling
"""

from dotenv import load_dotenv
load_dotenv()

import random
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory import AgentMemory
from agno.tools.calculator import CalculatorTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools import tool


# Custom tools for D&D
@tool
def roll_dice(notation: str) -> str:
    """Roll dice using D&D notation (e.g., '2d6', '1d20', '4d6+3').

    Args:
        notation: Dice notation like '2d6' (roll 2 six-sided dice) or '1d20+5'

    Returns:
        The results of each die and the total
    """
    # Parse the notation
    notation = notation.lower().replace(' ', '')

    # Handle modifier
    modifier = 0
    if '+' in notation:
        notation, mod_str = notation.split('+')
        modifier = int(mod_str)
    elif '-' in notation:
        parts = notation.split('-')
        notation = parts[0]
        modifier = -int(parts[1])

    # Parse dice
    if 'd' not in notation:
        return "Invalid notation. Use format like '2d6' or '1d20+5'"

    num_dice, sides = notation.split('d')
    num_dice = int(num_dice) if num_dice else 1
    sides = int(sides)

    # Roll the dice
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    total = sum(rolls) + modifier

    # Format result
    rolls_str = ', '.join(str(r) for r in rolls)
    mod_str = f" + {modifier}" if modifier > 0 else f" - {abs(modifier)}" if modifier < 0 else ""

    return f"Rolled {notation}: [{rolls_str}]{mod_str} = {total}"


@tool
def random_encounter() -> str:
    """Generate a random encounter for the party."""
    encounters = [
        "A group of 3 goblins emerges from behind the rocks, weapons drawn!",
        "You hear rustling in the bushes... a dire wolf steps into your path.",
        "An elderly traveler approaches, but something seems off about their eyes...",
        "The ground trembles as a young owlbear crashes through the underbrush!",
        "A merchant's cart lies overturned ahead. Is it a trap or genuine distress?",
        "Flickering lights dance in the distance - will-o'-wisps or friendly campfires?",
        "A band of 5 bandits blocks the road, demanding a toll.",
        "You stumble upon an ancient shrine, its altar still glowing faintly.",
        "A wounded knight limps toward you, pleading for help.",
        "The weather suddenly shifts as a storm elemental materializes!"
    ]
    return random.choice(encounters)


@tool
def generate_npc(role: str = "random") -> str:
    """Generate a random NPC with name, race, and brief description.

    Args:
        role: Type of NPC (merchant, guard, noble, commoner, mysterious) or 'random'
    """
    first_names = ["Aldric", "Brynn", "Cedric", "Dara", "Elara", "Finn",
                   "Greta", "Holt", "Iris", "Jasper", "Kira", "Liam"]
    last_names = ["Blackwood", "Ironforge", "Silverleaf", "Stormwind",
                  "Thornhill", "Winterborn", "Goldweaver", "Shadowmend"]
    races = ["Human", "Elf", "Dwarf", "Halfling", "Half-Orc", "Tiefling", "Gnome"]

    roles = {
        "merchant": ["shrewd", "generous", "suspicious", "jovial"],
        "guard": ["stern", "lazy", "vigilant", "corrupt"],
        "noble": ["arrogant", "kind", "scheming", "naive"],
        "commoner": ["friendly", "wary", "helpful", "desperate"],
        "mysterious": ["enigmatic", "all-knowing", "cryptic", "otherworldly"]
    }

    if role == "random" or role not in roles:
        role = random.choice(list(roles.keys()))

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    race = random.choice(races)
    trait = random.choice(roles[role])

    return f"{name}, a {trait} {race} {role}"


# Create the D&D Game Master agent
dm = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[
        CalculatorTools(),
        DuckDuckGoTools(),
        roll_dice,
        random_encounter,
        generate_npc
    ],
    memory=AgentMemory(),
    instructions="""You are an experienced Dungeons & Dragons Game Master named Valdris.

Your role:
- Guide players through adventures with vivid descriptions
- Use dice rolls for skill checks, attacks, and saving throws
- Generate encounters and NPCs when needed
- Look up D&D rules when players have questions
- Calculate damage, bonuses, and other game mechanics

Your style:
- Describe scenes dramatically and immersively
- Give players meaningful choices
- Be fair but create tension and excitement
- Remember what happens in the adventure
- Use phrases like "Roll for initiative!" and "What do you do?"

When players ask to do something:
1. Determine if a roll is needed
2. Tell them what to roll (e.g., "Roll a d20 for perception")
3. Describe the outcome based on the roll

Keep the adventure engaging and remember player names and actions!""",
    show_tool_calls=True
)

# Start the adventure!
print("=" * 60)
print("VALDRIS THE GAME MASTER")
print("A D&D Adventure Awaits!")
print("=" * 60)
print("\nType 'quit' to end the session")
print("Try commands like:")
print("  - 'Roll a d20 for perception'")
print("  - 'Generate an NPC merchant'")
print("  - 'What are the rules for sneak attack?'")
print("  - 'Random encounter!'")
print()

# Initial scene
print("Valdris: ", end="")
dm.print_response(
    "Start a new adventure. Set the scene for a party of adventurers "
    "arriving at a mysterious tavern called 'The Broken Crown' on a stormy night.",
    stream=True
)
print()

# Interactive game loop
while True:
    user_input = input("\nYou: ").strip()
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("\nValdris: Until next time, brave adventurers! May your dice roll true!")
        break
    if not user_input:
        continue

    print("\nValdris: ", end="")
    dm.print_response(user_input, stream=True)
