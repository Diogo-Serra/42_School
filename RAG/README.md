# RAG Against the Machine

This project is present here: https://github.com/Diogo-Serra/RAG

---

A Retrieval-Augmented Generation system that answers questions about the vLLM codebase. The system ingests the repository, splits Python and Markdown files with two dedicated chunking strategies, and builds a persistent lexical index using BM25 or TF-IDF. Given a question, it retrieves the most relevant source locations (file path and character range), passes them as context to the Qwen3-0.6B language model, and generates a structured answer grounded in those sources. Retrieval quality is measured with recall@k against ground-truth datasets, while respecting strict limits on indexing time, retrieval throughput and chunk size. The goal is to return the right evidence from a large codebase and produce faithful answers from it, through a command-line interface with validated data models.
