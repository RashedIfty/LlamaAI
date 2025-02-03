import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import Tool
from langchain.tools import WikipediaQueryRun, DuckDuckGoSearchRun, ArxivQueryRun
from langchain.memory import ChatMessageHistory
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)

vectorstore = Chroma(embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))
history = ChatMessageHistory()

def save_conversation(user_input, ai_response):
    history.add_user_message(user_input)
    history.add_ai_message(ai_response)
    vectorstore.add_texts([user_input, ai_response])

def search_wikipedia(query):
    return WikipediaQueryRun().run(query)

def search_duckduckgo(query):
    return DuckDuckGoSearchRun().run(query)

def search_arxiv(query):
    return ArxivQueryRun().run(query)

def math_solver(expression):
    return eval(expression)

def reverse_text(text):
    return text[::-1]


def download_conversation():
    conversation_text = ""
    for message in history.messages:
        role = "You" if message.type == "human" else "AI"
        conversation_text += f"{role}: {message.content}\n\n"
    return conversation_text

tools = [
    Tool(name="Wikipedia Search", func=search_wikipedia, description="Search Wikipedia for information"),
    Tool(name="DuckDuckGo Search", func=search_duckduckgo, description="Search the web using DuckDuckGo"),
    Tool(name="ArXiv Research Papers", func=search_arxiv, description="Search academic papers from ArXiv"),
    Tool(name="Math Solver", func=math_solver, description="Solve basic mathematical expressions"),
    Tool(name="Text Reverser", func=reverse_text, description="Reverse a given text string")
]

st.title("LlamaAI")
st.write("Chat with an AI powered by Groq's Llama-3.3-70b-versatile!")

# Store messages in a session state variable
if 'history_display' not in st.session_state:
    st.session_state.history_display = []

user_input = st.text_input("You:")
if user_input:
    response = llm.invoke([("human", user_input)])
    save_conversation(user_input, response.content)
    st.session_state.history_display.append(("You", user_input))
    st.session_state.history_display.append(("AI", response.content))
    st.write("AI:", response.content)

# Display conversation history
st.write("### Conversation History")
for role, message in st.session_state.history_display:
    st.write(f"*{role}:* {message}")

# Download conversation button
conversation_text = download_conversation()
st.download_button("Download Conversation", conversation_text, file_name="conversation.txt", mime="text/plain")

#streamlit run "D:\A UDEMY\__Project__\Project 3\main.py"