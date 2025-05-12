from sentence_transformers import SentenceTransformer

# You can swap to other models like 'all-mpnet-base-v2' or use OpenAI embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return model.encode(text)
