
# Finance News Research Chatbot 📈

This project allows you to input news article URLs, embed their contents, and then ask questions using LLMs (like Mixtral via Groq).

## Setup

1. Clone this repo or unzip it.
2. Create a `.env` file based on `.env.example` and put your API keys.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Embed URLs by running:
    ```bash
    python embed_urls.py
    ```
5. Run the app:
    ```bash
    streamlit run app.py
    ```

## APIs Used

- **Google Generative AI Embeddings** for vector storage.
- **Groq (Mixtral)** for answering queries.
