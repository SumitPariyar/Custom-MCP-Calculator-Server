📟 MCP Math Chat

An interactive math assistant built using MCP (Modular Chat Platform), LangGraph, and Google Gemini AI, designed to perform math operations in real-time through a Streamlit web interface.

This project demonstrates the integration of a custom MCP server with advanced AI models to create a tool-enabled conversational agent.

Features

Add, Multiply, Divide numbers.

Calculate Square Roots and Factorials.

Interactive Streamlit interface for live user queries.

AI-powered reasoning with tool integration.

Handles errors gracefully (e.g., division by zero, negative factorials, negative square roots).

Tools & Technologies Used

Python 3.11+

MCP (FastMCP) – For creating a modular server with callable tools.

LangGraph – For building state-driven agent workflows.

LangChain MCP Adapters – To connect the MCP server with AI models.

Google Gemini AI – Generative AI model to reason about math queries.

Streamlit – Interactive web UI.

dotenv – Load environment variables securely.

asyncio – For asynchronous execution in Python.

Installation

Clone the repository

git clone https://github.com/your-username/mcp-math-chat.git
cd mcp-math-chat


Create a virtual environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables
Create a .env file in the project root:

GEMINI_API_KEY=YOUR_GOOGLE_GENIE_API_KEY

Usage
1. Run the MCP Math Server
python custom_mcp_server.py


The server exposes endpoints to process math operations like add, multiply, divide, square root, and factorial.

2. Run the Streamlit App
streamlit run app.py


Enter any math-related question in the input box.

Click Send to get the answer.

The AI model processes your query and uses the MCP tools for calculation.

Example Queries

Add 45 and 32

What is 12 factorial?

Square root of 256

Divide 100 by 4

Multiply 23 and 19

How It Works

MCP Server: Hosts math tools (add, multiply, division, square_root, factorial) that can be called programmatically.

MCP Client: Connects to the server, fetches available tools, and makes them accessible to the AI model.

LangGraph: Manages the conversational state and decides when to invoke tools vs. responding directly.

Google Gemini AI: Processes user input, reasons about it, and uses the tools to produce accurate math results.

Streamlit: Provides a live, interactive web interface to chat with the math assistant.

Project Structure
mcp-math-chat/
│
├── custom_mcp_server.py   # MCP server with math tools
├── app.py                 # Streamlit UI + AI integration
├── .env                   # Environment variables (API keys)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

Notes

Make sure the MCP server is running before using the Streamlit app.

The app supports async operations using asyncio to handle real-time responses.

Error handling is implemented for invalid operations like division by zero or negative factorials.

License

MIT License © 2025 Sumit Pariyar
