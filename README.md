This is a trading virtual coach RAG testing. 

High Architecture for a MVP is as follow: 
My trades → SQLite → trade documents → VectorDB → retriever → LangAPI → local LLM → trade coaching output


SQLite
= exact structured facts
= count trades, sum PnL, filter ticker, filter date

Trade Documents
= my trades documented over a period of time 

Vector DB
= meaning search
= find trades similar to "I froze", "failed to cut", "oversized", "broke rules"
A “vector row” is usually one searchable text block plus metadata.
*document formatting affects answer quality. Messy Context  = Messy or missed returns*

For RAG document formatting, f"""...""" is usually easier to read. multi-f strings