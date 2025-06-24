
import os
import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# Background setup
def set_bg_from_local(image_path):
    import base64
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    ext = image_path.split(".")[-1]
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{ext};base64,{encoded}) no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """, unsafe_allow_html=True
    )

# Streamlit UI
st.title("Finance News Research Chatbot 📈")
set_bg_from_local("assets/background.jpg")

# Load Chroma vector store
persist_directory = "news_chroma_store"
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Initialize model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
memory = ConversationBufferWindowMemory(memory_key='chat_history', return_messages=True)

# Setup QA chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectordb.as_retriever(search_kwargs={"k": 5}),
    memory=memory
)

# User input
user_question = st.text_input("Ask a question based on the processed news articles:")
if user_question:
    response = qa_chain.invoke({"question": user_question})
    st.write(response['answer'])
