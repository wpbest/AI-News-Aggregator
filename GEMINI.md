# AI-News-Aggregator: Technical Architecture & Implementation

This document provides a deep dive into the architecture, technology stack, and implementation details of the AI-News-Aggregator.

---

## 1. Overview & Architecture

The AI-News-Aggregator is a **modular, pipeline-based system** designed to automate the collection, processing, summarization, and personalized curation of AI-related news from diverse sources (YouTube, OpenAI, Anthropic).

### High-Level Workflow:
1.  **Ingestion**: Scrapers fetch the latest content (RSS feeds, YouTube metadata).
2.  **Processing**: Content is converted into machine-readable formats (Markdown extraction, YouTube transcripts).
3.  **Digestion**: An LLM-based agent generates concise summaries (Digests) for each item.
4.  **Curation**: A second LLM-based agent ranks these digests against a **User Profile** to find the most relevant content.
5.  **Delivery**: The top-ranked results are formatted and sent via email.

---

## 2. Technology Stack

### Core Technologies:
-   **Language**: Python 3.12+
-   **Database**: PostgreSQL (Relational)
-   **ORM**: SQLAlchemy 2.0
-   **LLM Provider**: Google Gemini (**Unified `google-genai` SDK**)
-   **Primary Model**: **Gemini 2.5 Flash-Lite** (2026 Workhorse)
-   **Embedding Model**: Google **Text Embedding 004** (Current Stable)
-   **Parsing & Extraction**:
    -   `Docling`: Advanced document parsing to Markdown.
    -   `BeautifulSoup4`: Web scraping and HTML parsing.
    -   `Feedparser`: RSS/Atom feed processing.
    -   `Markdownify`: HTML to Markdown conversion.
-   **APIs**: `youtube-transcript-api` for automated transcript retrieval.

---

## 3. Data Ingestion & Scrapers

The system uses specialized scrapers for different content sources, managed via `app/scrapers/`:

-   **YouTube Scraper**: Fetches metadata (title, URL, description) and uses `youtube-transcript-api` to pull full transcripts.
-   **OpenAI/Anthropic Scrapers**: Utilize RSS feeds to detect new blog posts. `Docling` is used to clean the HTML and extract high-quality Markdown content for processing.

Data is stored in a structured relational schema (`app/database/models.py`) with tables for:
-   `YouTubeVideo`
-   `OpenAIArticle`
-   `AnthropicArticle`
-   `Digest` (The summarized and processed version of an article/video)

---

## 4. Agentic Layer & RAG Implementation

The system uses a **Hybrid RAG** approach, combining traditional metadata filtering with modern vector-based semantic search.

### RAG Strategy (Semantic Search & Ranking):
1.  **Vector Database**: Uses `pgvector` in PostgreSQL to store 768-dimensional embeddings.
2.  **Embedding Generation**: Uses Google's **Text Embedding 004** via the unified `client.models.embed_content` interface.
3.  **Semantic Retrieval**: 
    -   The system performs **Cosine Similarity** searches across the entire database to find content semantically related to a user's interests.
4.  **Digest-then-Rank**: For daily updates, the system uses the LLM's context window to perform a global ranking of the day's items against the **User Profile**.

### Technology Implementation:
-   **Database Column**: `embedding = Column(Vector(768))` in `app/database/models.py`.
-   **Service**: `EmbeddingService` in `app/services/embedding.py` handles API calls using the centralized `genai.Client`.
-   **Repository**: `Repository.semantic_search` provides the interface for vector queries.

---

## 5. Implementation Details

### Embedding Service (`app/services/embedding.py`)
-   **Model**: `text-embedding-004`.
-   **Dimensions**: 768.
-   **SDK**: `google-genai`.

### Digest Agent (`app/agent/digest_agent.py`)
-   **Model**: `gemini-2.5-flash-lite`.
-   **SDK**: Unified `google-genai` Client.
-   **Feature**: Native Pydantic structured output (`response.parsed`).

### Curator Agent (`app/agent/curator_agent.py`)
-   **Model**: `gemini-2.5-flash-lite`.
-   **Goal**: Personalized ranking using structured JSON output.

### Repository Pattern (`app/database/repository.py`)
A centralized repository handles all database interactions, providing a clean abstraction for the agents and services to fetch "undigested" content or store new rankings.

---

## 6. Future Directions

-   **Hybrid Search**: Implementing `pgvector` in PostgreSQL to allow for historical search alongside daily ranking.
-   **Local Embeddings**: Moving to local embedding models (e.g., `sentence-transformers`) for initial filtering before LLM ranking.
-   **Multi-Agent Feedback**: A feedback loop where the user can "like/dislike" articles in the email, updating the `USER_PROFILE` dynamically.
