import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, MessagesState, START, END
import streamlit as st
from langchain.schema import HumanMessage



# Load environment variables from .env if needed
load_dotenv()

GEMINI_API_KEY = "AIzaSyBDSDB36zgcEHFy11oVI3tAt5I6vr6xZHo"

# -------------------------------
# Async MCP + LangGraph function
# -------------------------------
async def run_mcp_query(user_input: str):
    # Initialize Google Gemini model
    model = ChatGoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        api_key=GEMINI_API_KEY
    )

    # Initialize MCP client
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "streamable_http",
                "url": "http://127.0.0.1:8000/mcp"
            }
        }
    )

    # Fetch tools from MCP client
    tools = await client.get_tools()

    # Bind tools to model
    model_with_tools = model.bind_tools(tools)

    # Decide whether to continue or end
    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END

    # Function to call the model
    async def call_model(state: MessagesState):

    # Ensure the last message is wrapped in HumanMessage
        last_message_text = state["messages"][-1]

        if isinstance(last_message_text, str):
            last_message_text = HumanMessage(content=last_message_text)

        response = await model_with_tools.ainvoke([last_message_text])

        return {"messages": [response]}



    # Placeholder for tools node
    async def tools_node(state: MessagesState):
        # Here you can process tool calls manually if needed
        return state

    # Build the StateGraph
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", tools_node)
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", should_continue)
    builder.add_edge("tools", "call_model")

    # Compile the graph
    graph = builder.compile()

    # Run the graph
    result = await graph.ainvoke({
    "messages": [HumanMessage(content=user_input)]
})



    return result["messages"][-1].content if hasattr(result["messages"][-1], "content") else str(result)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="MCP Math Chat", page_icon="📟")
st.title("📟 MCP Math Chat (Streamlit)")

user_input = st.text_input("Ask me something math-related:")


if st.button("Send") and user_input.strip():
    import nest_asyncio
    nest_asyncio.apply()  # allow nested asyncio loops in Streamlit

    with st.spinner("Thinking..."):
        answer = asyncio.run(run_mcp_query(user_input))
        st.success(answer)
