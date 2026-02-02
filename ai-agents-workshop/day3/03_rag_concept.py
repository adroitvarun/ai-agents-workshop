"""
Day 3: RAG Concept (Conceptual - Don't Run in Workshop)

This file shows what RAG looks like in Agno.
We won't implement this today, but it's your next learning step!

RAG = Retrieval-Augmented Generation
It lets agents access large documents or databases.
"""

# This is CONCEPTUAL CODE - it requires additional setup
# (PostgreSQL with pgvector, document files, etc.)

"""
# How RAG works conceptually:

# 1. SETUP PHASE (done once)
# - Take your documents (PDFs, text files, etc.)
# - Split them into chunks
# - Convert chunks to "embeddings" (numbers that capture meaning)
# - Store in a vector database

from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector

knowledge = PDFKnowledgeBase(
    path="path/to/your/documents/",
    vector_db=PgVector(
        table_name="documents",
        db_url="postgresql://localhost:5432/mydb"
    )
)

# Load documents into the database (run once)
knowledge.load()


# 2. QUERY PHASE (every request)
# - User asks a question
# - Agent searches the knowledge base for relevant chunks
# - Relevant chunks are added to the prompt
# - LLM answers based on your actual documents!

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    knowledge=knowledge,
    search_knowledge=True,  # Enable automatic searching
    instructions="Answer based on the provided documents. Cite your sources."
)

agent.print_response("What is our company's refund policy?")
# The agent will search your docs and give an accurate answer!
"""

print("=" * 50)
print("RAG: YOUR NEXT LEARNING STEP")
print("=" * 50)
print("""
RAG (Retrieval-Augmented Generation) lets you:

- Chat with your own documents
- Build customer support agents that know your products
- Create research assistants with access to papers
- Make agents that remember across sessions

Key concepts:

1. EMBEDDINGS
   Numbers that capture meaning.
   "happy" and "joyful" have similar embeddings.
   This lets us search by meaning, not just keywords.

2. VECTOR DATABASE
   A database optimized for similarity search.
   "Find me chunks similar to this question."

3. RAG FLOW
   Question -> Find relevant chunks -> Add to prompt -> LLM answers

Example use cases:
- "What's our refund policy?" (searches company docs)
- "Summarize the key findings" (searches research papers)
- "How do I configure X?" (searches documentation)

To learn more:
- Agno docs: https://docs.agno.com/knowledge
- Try the PDF knowledge base example in Agno's cookbook

Required setup (not covered in this workshop):
- PostgreSQL with pgvector extension
- OR another vector database (Pinecone, Weaviate, etc.)
- Document files to index
""")
