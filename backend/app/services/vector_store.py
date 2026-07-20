import os
import chromadb


class VectorStore:

    def __init__(self):

        base_dir = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../..")
        )

        db_path = os.path.join(
            base_dir,
            "data",
            "chroma_db"
        )

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(self, chunks, embeddings):

        ids = []

        for i in range(len(chunks)):
            ids.append(f"chunk_{i}")

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )

        print(f"{len(chunks)} chunks stored successfully.")
        
    def search(self, query_embedding, n_results=3):

     results = self.collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

     return results
        
        
