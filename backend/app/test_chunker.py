from services.document_loader import DocumentLoader
from services.text_chunker import chunk_text

# Path to your PDF
pdf_path = r"D:\agentic-ai-learning-assistant\agentic-ai-learning-assistant\data\uploads\sample.pdf"

# Extract text from PDF
text = DocumentLoader.read_pdf(pdf_path)

# Create chunks
chunks = chunk_text(text)

# Print results
print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\n----- Chunk {i} -----")
    print(chunk)
    
    
from services.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

embeddings = embedding_service.generate_embeddings(chunks)

print(f"\nTotal Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")