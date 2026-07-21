import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from services.retriever import Retriever

retriever = Retriever()

question = "Explain Nyquist Bit Rate"

documents = retriever.retrieve(question)

print("\nRetrieved Documents\n")

for i, doc in enumerate(documents):

    print("=" * 60)
    print(f"Result {i+1}\n")
    print(doc)