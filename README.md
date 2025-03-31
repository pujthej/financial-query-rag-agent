Financial Query RAG Agent
A full-stack, Retrieval-Augmented Generation (RAG) agent that can explain financial concepts and analyze stock market trends — powered by LangGraph, LangChain, FastAPI, and a sleek React frontend.

This project demonstrates the complete lifecycle of building and serving an LLM-based RAG agent, from development to deployment. 
It supports financial queries using:
✅ Wikipedia-based RAG for domain knowledge
✅ Finnhub API for real-time stock market news
✅ PostgreSQL for chat history persistence
✅ React + Vite + Tailwind CSS for a beautiful UI

Features
1. Retrieve and explain financial terms (via Wikipedia)
2. Track stock trends using Finnhub’s news API
3. Agent architecture with LangGraph + LangChain
4. Vector store powered by FAISS
5. PostgreSQL-backed persistent memory
6. REST API with FastAPI
7. Responsive chat UI (React + Tailwind)

Tech Stack
Frontend - React, Vite, Tailwind CSS
Backend - FastAPI, LangChain, LangGraph, HuggingFace Transformers
Data Store - PostgreSQL (Chat logs), FAISS (Embeddings)
APIs - OpenAI (GPT-4o-mini), Finnhub
