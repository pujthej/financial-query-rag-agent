from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessagesState
from langgraph.prebuilt import ToolNode
from typing import Literal
from langchain_core.messages import HumanMessage
from .tools import get_tools

tools = get_tools()
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)

def agent(state: MessagesState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)

def should_continue(state: MessagesState) -> Literal["tools", END]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

