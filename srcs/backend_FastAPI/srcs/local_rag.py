from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from custom_chain import run_rag_on_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RAGQuery(BaseModel):
    query: str
    collection_name: str

@app.post("/api/rag/query")
def query_rag(data: RAGQuery):
    answer = run_rag_on_collection(data.query, data.collection_name)
    return {"answer": answer}