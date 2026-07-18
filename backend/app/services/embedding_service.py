from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Model loaded successfully!")

    def generate_embeddings(self, chunks):
        embeddings = self.model.encode(chunks)

        return embeddings