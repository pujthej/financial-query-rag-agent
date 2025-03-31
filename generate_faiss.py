from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load links
with open('links.txt', 'r') as f:
    links = list(set(link.strip() for link in f.readlines()))

# Load documents from web
print("Loading documents...")
docs = WebBaseLoader(links).load()

# Split into semantic chunks
print("Splitting documents...")
splitter = SentenceTransformersTokenTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = splitter.split_documents(docs)

# Create embeddings
print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embeddings.client.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

# Save FAISS index
print("Saving FAISS index to 'faiss_index' folder...")
db = FAISS.from_documents(chunks, embedding=embeddings)
db.save_local("faiss_index")

print("FAISS index created and saved.")
