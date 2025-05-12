from embedding import get_embedding
from vectorstore import VectorIndex

data = [
    "OpenAI launches ChatGPT.",
    "Apple releases the new iPhone.",
    "Researchers propose a new LLM model.",
    "Reddit discusses large language models.",
    "NASA finds water on Mars."
]

embeddings = [get_embedding(t) for t in data]

index = VectorIndex(dimension=len(embeddings[0]))
index.add(embeddings, data)

query = "What are the latest developments in AI?"
query_embedding = get_embedding(query)

results = index.search(query_embedding)
print("🔍 Top matches for:", query)
for r in results:
    print(" -", r)
