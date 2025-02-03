# LlamaAI: Chat with an AI Powered by Groq's Llama-3.3-70b-Versatile


![2025-02-03 18_21_20-Settings](https://github.com/user-attachments/assets/6fe7c1b1-bbd2-4c8f-ab41-ec8ac46b2080)




## Overview
LlamaAI is an interactive AI chat application that uses Groq's Llama-3.3-70b-versatile model to provide users with intelligent responses. This mini-project leverages the capabilities of Groq's hardware for accelerated AI inference, integrating various useful tools to extend the functionality of the chat interface.

Key Features:
- Interactive chat with a Groq-powered Llama AI model.
- Access to multiple external tools such as Wikipedia, DuckDuckGo, ArXiv, a math solver, and a text reverser.
- History of the conversation stored and displayed for review.
- Option to download the conversation in plain text format.

## Requirements

- Python 3.8 or later
- Streamlit
- LangChain
- Groq API Key (`GROQ_API_KEY`)
- Python packages: `streamlit`, `os`, `dotenv`, `langchain`, `langchain_groq`, `langchain_core`

### Installation

1. Clone the repository or download the project files.
2. Install the required Python packages using `pip`:

   ```bash
   pip install streamlit langchain langchain_groq dotenv
   ```

3. Create a `.env` file in the project directory and add your Groq API Key:
   
   ```text
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Features

### 1. **AI Chat:**
   Users can interact with an AI model powered by Groq's Llama-3.3-70b-versatile to get responses in natural language. The conversation history is saved and displayed in real time.

### 2. **External Tools:**
   - **Wikipedia Search:** Search Wikipedia articles for any given query.
   - **DuckDuckGo Search:** Perform web searches using DuckDuckGo.
   - **ArXiv Research Papers:** Search for academic papers on ArXiv.
   - **Math Solver:** Solve basic mathematical expressions.
   - **Text Reverser:** Reverse any text string.

### 3. **Conversation History:**
   The conversation history is stored and displayed in the UI, allowing users to review previous messages.

### 4. **Download Conversation:**
   After the conversation ends, users can download the entire conversation as a `.txt` file.

## How to Use

1. Launch the Streamlit app by running `streamlit run app.py`.
2. Enter your text in the input box.
3. The AI will respond with an intelligent answer based on the Llama-3.3-70b-versatile model.
4. You can interact with various tools such as Wikipedia search or a math solver by inputting specific commands.
5. The conversation history will be displayed, and you can download the entire conversation as a `.txt` file by clicking the "Download Conversation" button.

## Code Structure

- **app.py**: Main Streamlit application script.
- **.env**: File containing your Groq API key.
- **requirements.txt**: File listing the necessary Python packages.

## Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests. Contributions to improve the project are always welcome!


