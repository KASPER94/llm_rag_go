import os
import streamlit as st
import chromadb
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from chromadb.config import Settings

chroma_host = os.getenv("CHROMA_HOST", "localhost")
chroma_port = int(os.getenv("CHROMA_PORT", 7000))

st.title("🧠 RAG avec LangChain + Chroma")

uploaded_file = st.file_uploader("Charge un PDF", type=["pdf"])
question = st.text_input("Pose une question sur le document")

if uploaded_file and question:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print(f"Tentative de connexion à ChromaDB sur {chroma_host}:{chroma_port}")

    chroma_client = chromadb.HttpClient(
        host=chroma_host,
        port=chroma_port
    )

    vectordb = Chroma(
        collection_name="rag_collection",
        embedding_function=embeddings,
        client=chroma_client
    )

    vectordb.add_documents(chunks)

    retriever = vectordb.as_retriever()
    llm = Ollama(model="gemma:2b", base_url="http://llm:11434")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    # qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(temperature=0), retriever=retriever)

    result = qa_chain.run(question)
    st.write("### Réponse :")
    st.write(result)