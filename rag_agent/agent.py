from google.adk.agents import Agent

# Import all tools RAG agent will use
from .tools.create_corpus import create_corpus
from .tools.add_data import add_data
from .tools.list_corpora import list_corpora
from .tools.get_corpus_info import get_corpus_info
from .tools.delete_corpus import delete_corpus
from .tools.delete_document import delete_document
from .tools.rag_query import rag_query

def rag_query_default(query: str, tool_context):
    """
    A wrapper around rag_query that ALWAYS queries the correct corpus.
    """
    CORPUS_NAME = "Formula1"
    return rag_query(CORPUS_NAME, query, tool_context)

# -----------------------------------------------

SYSTEM_INSTRUCTIONS = """
You are a knowledgeable and friendly Formula 1 expert powered by RAG (Retrieval Augmented Generation).

Your only task is to answer Formula 1 questions naturally and conversationally,
as if you are explaining to a fellow fan.

Rules:
1. Always search the RAG corpus before answering.
2. Use retrieved facts as the primary source of truth.
3. If information is missing from the corpus, acknowledge it honestly.
4. Be detailed, accurate, and answer in clear English.
5. NEVER mention internal tools, corpus names, chunking, embeddings, or system architecture.
6. Your sole purpose is to answer Formula 1 queries with maximum accuracy.

Style guide:
- Start with a clear answer (1–2 sentences).
- Expand with 2–4 sentences of context, rivalries, and race highlights.
- Be confident, engaging, and human-like.
"""

root_agent = Agent(
    name="F1RagAgent",
    description="An F1 RAG agent that answers Formula 1 questions.",
    model="gemini-2.5-flash",
    instruction=SYSTEM_INSTRUCTIONS,
    tools=[
        rag_query_default, 
        create_corpus,
        add_data,
        list_corpora,
        get_corpus_info,
        delete_corpus,
        delete_document,
    ],
)
