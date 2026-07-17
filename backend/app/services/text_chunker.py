"""
Text Chunking Service
Splits large text into smaller chunks for embeddings and RAG.
"""


def chunk_text(text, chunk_size=500):
    """
    Split text into chunks of fixed size.

    Args:
        text (str): Input text
        chunk_size (int): Number of characters per chunk

    Returns:
        list: List of text chunks
    """

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


if __name__ == "__main__":
    sample_text = """
    Agentic AI systems are autonomous AI systems capable of
    reasoning, planning, memory, and tool usage.
    """

    chunks = chunk_text(sample_text, chunk_size=50)

    print(f"Total Chunks: {len(chunks)}")

    for idx, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {idx}")
        print(chunk)