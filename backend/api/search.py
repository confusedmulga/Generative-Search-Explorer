from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.semantic.embedding import get_embedding
from backend.semantic.vectorstore import VectorIndex
from backend.rag.generator import generate_answer

router = APIRouter()

# Mock knowledge base for now (replacing with real source later)
docs = [
    "OpenAI launched GPT-4, a powerful new language model.",
    "Researchers discovered a new quantum computing algorithm.",
    "Reddit users are discussing large language models.",
    "Tesla reveals plans for autonomous robotaxis.",
    "NASA confirms a new Mars rover mission."
]

embeddings = [get_embedding(doc) for doc in docs]
index = VectorIndex(dimension=len(embeddings[0]))
index.add(embeddings, docs)

class SearchRequest(BaseModel):
    query: str

@router.post("/search")
def semantic_search(request: SearchRequest):
    try:
        query_embedding = get_embedding(request.query)
        top_docs = index.search(query_embedding, top_k=3)
        answer = generate_answer(top_docs, request.query)
        return {
            "query": request.query,
            "top_matches": top_docs,
            "generated_answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
