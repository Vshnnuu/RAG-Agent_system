from rag_agent.tools.get_corpus_info import get_corpus_info

class FakeToolContext:
    def __init__(self):
        self.state = {}

tool_context = FakeToolContext()

CORPUS_NAME = "Formula1"

def main():
    result = get_corpus_info(CORPUS_NAME, tool_context)

    if result.get("status") != "success":
        print(result)
        return

    files = result.get("files", [])
    file_count = len(files)

    print("\n=== Corpus Summary ===")
    print(f"Corpus: {CORPUS_NAME}")
    print(f"Total files: {file_count}")

    # Optional: show only the first 10 files
    print("\nFirst 10 files:")
    for f in files[:10]:
        print(" -", f.get("display_name"))

    print("\n(Use ADK UI if you want to browse all files.)")

if __name__ == "__main__":
    main()
