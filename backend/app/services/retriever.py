from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(self, question, top_k=3):

        query_embedding = self.embedding_service.generate_embeddings(
            [question]
        )[0]

        results = self.vector_store.search(
            query_embedding,
            n_results=top_k
        )

        return results["documents"][0]