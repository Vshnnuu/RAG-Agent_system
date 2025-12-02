"""
Bootstrap script for the Formula1 RAG corpus.

This script:
  - Ensures the Formula1 corpus exists
  - Ingests all file paths from f1_manifest.txt (if not already added)
  - Prints final corpus info

Usage:
  python -m scripts.bootstrap_f1_corpus
"""

from rag_agent.tools.create_corpus import create_corpus
from rag_agent.tools.add_data import add_data
from rag_agent.tools.get_corpus_info import get_corpus_info


# -------------------------------------------------------
# Minimal ToolContext for running ADK tools outside UI
# -------------------------------------------------------
class FakeToolContext:
    def __init__(self):
        self.state = {}
        self.user_id = "bootstrap"


tool_context = FakeToolContext()

# -------------------------------------------------------
CORPUS_NAME = "Formula1"

# Read all file paths from manifest
with open("f1_manifest.txt", "r") as f:
    ALL_PATHS = [line.strip() for line in f if line.strip()]

BATCH_SIZE = 200  # Vertex safe batch size


def main():
    print("\n=== Creating Corpus ===")
    result = create_corpus(CORPUS_NAME, tool_context)
    print(result)

    print("\n=== Adding Files in Batches ===")
    for i in range(0, len(ALL_PATHS), BATCH_SIZE):
        batch = ALL_PATHS[i : i + BATCH_SIZE]
        print(f"\n-- Batch {i // BATCH_SIZE + 1}: {len(batch)} files --")

        result = add_data(CORPUS_NAME, batch, tool_context)
        print(result)

    print("\n=== Corpus Info ===")
    result = get_corpus_info(CORPUS_NAME, tool_context)
    print(result)

    print("\n=== Bootstrap Complete ===\n")


if __name__ == "__main__":
    main()
