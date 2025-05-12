from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from Generative Search Explorer"}

app.include_router(search.router)
