# Gemini + Pinecone Semantic Search

This project demonstrates how to build a **semantic search** and **Q&A system** using:

- **Google Gemini API** — for creating embeddings & generating LLM responses  
- **Pinecone Vector Database** — for storing and retrieving embeddings efficiently

You can store **long paragraphs** in Pinecone, embed them with Gemini, and then query them in natural language to retrieve the **most semantically relevant** content.

---

## 🚀 Features

- 📌 Embed text into vectors using **Google Gemini’s `text-embedding-004` model**
- 📦 Store embeddings in a **Pinecone vector database**
- 🔍 Search **by meaning** (semantic search) rather than exact keyword match
- 🤖 Generate answers using retrieved context with **`gemini-1.5-flash`**

---

## 🛠 Tech Stack

- Python 3.10+
- [Google Gemini API](https://ai.google.dev/)
- [Pinecone Vector Database](https://www.pinecone.io/)
- Libraries:
  - `pinecone-client`
  - `google-genai`
  - `os` for environment variables

---

## 📂 How It Works

1. **Get Input Content**  
   You provide text (a paragraph, article, etc.).

2. **Generate Embeddings**  
   Gemini converts the text into a **vector representation** (`text-embedding-004`).

3. **Store in Pinecone**  
   The vector + metadata (original text) is stored in Pinecone.

4. **User Query**  
   A user enters a natural language question.

5. **Vector Search**  
   The query is embedded with Gemini, and Pinecone finds the **closest matching vectors**.

6. **LLM Answer Generation**  
   The matching content is passed to **Gemini 1.5 Flash**, which generates a concise answer.

---

# 📦 Installation

## Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

## Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

# Notes

- You can store multiple documents with different IDs for richer search results.

- Pinecone searches by semantic similarity, so exact wording isn’t required.

- Large datasets can be indexed for scalable retrieval.
