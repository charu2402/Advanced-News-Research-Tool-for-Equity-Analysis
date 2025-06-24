
import os
import pickle
import requests
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# Get URLs
urls = [
    input("Enter URL 1: "),
    input("Enter URL 2: "),
    input("Enter URL 3: ")
]

valid_urls = [url for url in urls if url.strip() != ""]
loader = UnstructuredURLLoader(urls=valid_urls)
docs = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
final_documents = text_splitter.split_documents(docs)

# Metadata fix
for doc in final_documents:
    if 'source' in doc.metadata:
        doc.metadata['source'] = doc.metadata['source'].split('/')[-1]
    else:
        doc.metadata['source'] = "Unknown"

# Embedding and save
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(final_documents, embeddings, persist_directory="news_chroma_store")
vectorstore.persist()

print("Documents embedded and saved to news_chroma_store ✅")
