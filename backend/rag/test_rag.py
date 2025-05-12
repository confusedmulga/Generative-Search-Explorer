from backend.semantic.embedding import get_embedding
from backend.semantic.vectorstore import VectorIndex
from backend.rag.generator import generate_answer

docs = [
    "OpenAI launched GPT-4, a powerful new language model.",
    "Researchers discovered a new quantum computing algorithm.",
    "Reddit users are discussing large language models.",
    "Tesla reveals plans for autonomous robotaxis.",
    "NASA confirms a new Mars rover mission."
]

query = "What’s the latest news in AI?"

# Embed and build index
embeddings = [get_embedding(doc) for doc in docs]
index = VectorIndex(dimension=len(embeddings[0]))
index.add(embeddings, docs)

# Search and RAG generate
query_embedding = get_embedding(query)
top_docs = index.search(query_embedding, top_k=3)

answer = generate_answer(top_docs, query)
print("🧠 AI Response:\n", answer)
