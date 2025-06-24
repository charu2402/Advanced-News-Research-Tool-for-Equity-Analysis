import streamlit as st
from chatbot.chatbot import FinanceChatbot

bot = FinanceChatbot()

st.title("📈 Finance News Chatbot")

user_input = st.text_input("Ask me about a stock (e.g., 'Tell me about Reliance', 'Price of Infosys')")

if st.button("Ask"):
    response = bot.handle_query(user_input)
    st.write(response)

if st.button("🎤 Voice Mode"):
    response = bot.voice_mode()
    st.write(response)
