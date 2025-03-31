from langchain_core.tools import tool
import requests
import os
from langchain.tools.retriever import create_retriever_tool
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_retriever_tool():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 1})
    return create_retriever_tool(
        retriever,
        "explain_financial_terms",
        "Explain financial terms in the query"
    )

def news_helper(symbol: str, start_date: str, last_date: str):
    api_key = os.environ["FINNHUB_API_KEY"]
    url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={start_date}&to={last_date}&token={api_key}"
    res = requests.get(url)
    articles = res.json()[-5:]
    return ", ".join([a["summary"] for a in articles])

@tool
def search_news_for_symbol(symbol: str, start_date: str, last_date: str) -> str:
    """Get news for a stock ticker in a date range."""
    return news_helper(symbol, start_date, last_date)

def get_tools():
    return [get_retriever_tool(), search_news_for_symbol]

