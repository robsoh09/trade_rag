This is a trading virtual coach RAG testing. 

High Architecture as follow: 
My trades → SQL → trade documents → VectorDB → retriever → LangAPI → local LLM → trade coaching output


SQLite
= exact structured facts
= count trades, sum PnL, filter ticker, filter date

Vector DB
= meaning search
= find trades similar to "I froze", "failed to cut", "oversized", "broke rules"
A “vector row” is usually one searchable text block plus metadata.
