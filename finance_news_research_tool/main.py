import os
import streamlit as st
import pickle
import time
import requests
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader

# Load environment variables (optional)
#

# Gemini API details
GEMINI_API_KEY = "AIzaSyCPDYvBu3_kVfZA0wFCSJTv2A7snlF8AfQ"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def ask_gemini(prompt):
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(GEMINI_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['candidates'][0]['content']['parts'][0]['text']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Something went wrong. Please try again."

# Streamlit App
st.title("Finance News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Collect URLs from user input
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# Button to start processing URLs
process_url_clicked = st.sidebar.button("Process URLs")

# Main placeholder
main_placeholder = st.empty()

# File to save
file_path = "texts.pkl"

if process_url_clicked:
    # Filter out empty URLs
    valid_urls = [url for url in urls if url.strip() != ""]

    if not valid_urls:
        st.error("Please enter at least one valid URL.")
    else:
        # Load data
        loader = UnstructuredURLLoader(urls=valid_urls)
        main_placeholder.text("Data Loading... Started... ✅✅✅")
        data = loader.load()

        # Split data
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000
        )
        main_placeholder.text("Text Splitting... Started... ✅✅✅")
        docs = text_splitter.split_documents(data)

        texts = [doc.page_content for doc in docs]

        # Save texts
        with open(file_path, "wb") as f:
            pickle.dump(texts, f)
        
        main_placeholder.success("Texts Processed and Saved ✅✅✅")

# Query input
query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            texts = pickle.load(f)

        # Combine all texts into context
        context = "\n".join(texts[:5])  # limit to avoid token limit issues
        
        # Create a prompt
        full_prompt = f"Answer the following question based on the context below.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
        
        # Get answer from Gemini
        answer = ask_gemini(full_prompt)

        # Display
        st.header("Answer")
        st.write(answer)

