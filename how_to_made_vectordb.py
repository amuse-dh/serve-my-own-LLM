from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain.vectorstores import Chroma

loader = PyPDFLoader("C:/Users/DH/Desktop/논문/DetCo_Unsupervised Contrastive Learning for Object Detection.pdf")
docs = loader.load()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
splitter = SemanticChunker(embedding)
chunks = splitter.split_documents(docs)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./my_paper_vectordb"
)
db.persist() 