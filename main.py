from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from agent import get_graph
from langchain_core.messages import HumanMessage
from psycopg_pool import ConnectionPool
import os
from langgraph.checkpoint.postgres import PostgresSaver
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pool = ConnectionPool(conninfo=os.environ['DB_URI'], max_size=20, kwargs={"autocommit": True})

@app.get("/")
def query_llm(query: str) -> str:
    checkpointer = PostgresSaver(pool)
    checkpointer.setup()
    graph = get_graph(checkpointer)
    final_state = graph.invoke({"messages": [HumanMessage(content=query)]}, config={"configurable": {"thread_id": "1"}})
    return final_state["messages"][-1].content

@app.on_event("shutdown")
async def shutdown_event():
    pool.close()
