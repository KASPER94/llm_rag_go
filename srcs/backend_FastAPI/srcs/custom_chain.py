from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import chromadb

def run_rag_on_collection(query: str, collection_name: str):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    chroma_client = chromadb.HttpClient(host="localhost", port=7000)

    vectordb = Chroma(
        client=chroma_client,
        collection_name=collection_name,
        embedding_function=embeddings
    )
    
    retriever = vectordb.as_retriever()
    llm = Ollama(model="gemma:2b", base_url="http://llm:11434")
    
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)
