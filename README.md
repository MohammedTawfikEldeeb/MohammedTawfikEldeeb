<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./dark_mode.svg">
  <source media="(prefers-color-scheme: light)" srcset="./light_mode.svg">
  <img src="./light_mode.svg" alt="Mohamed Tawfik profile header">
</picture>

<br>

<a href="https://github.com/MohammedTawfikEldeeb">
  <img src="https://img.shields.io/badge/GitHub-MohammedTawfikEldeeb-181717?style=for-the-badge&logo=github" />
</a>
<a href="https://www.linkedin.com/in/mohamed-tawfik-aaa4562a3/">
  <img src="https://img.shields.io/badge/LinkedIn-Mohamed%20Tawfik-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:mohamed.tawfik.eldeeb@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=MohammedTawfikEldeeb&style=for-the-badge&color=0969da" alt="Profile views">

</div>

---

## About

**AI Engineer & Software Engineer** focused on building production-oriented intelligent systems.

My work combines **Generative AI, Agentic Systems, RAG, real-time voice applications, backend engineering, and MLOps**. I build systems end-to-end: from retrieval and tool-calling logic to APIs, databases, observability, evaluation, and deployment.

```text
AI ENGINEERING
    ├── Agentic AI
    │   ├── LangGraph / LangChain
    │   ├── MCP / Tool Calling
    │   ├── Memory / State
    │   └── Human-in-the-loop
    │
    ├── Retrieval & RAG
    │   ├── Dense Retrieval
    │   ├── BM25 / Hybrid Search
    │   ├── RRF Fusion
    │   └── Cross-Encoder Reranking
    │
    └── Production Engineering
        ├── FastAPI / Flask
        ├── Node.js / Express.js
        ├── JavaScript / TypeScript
        ├── SQL / PostgreSQL
        └── Docker / AWS / MLOps
```

---

# Tech Stack

### Languages

<p>
  <img src="https://skillicons.dev/icons?i=python,js,ts,sql,bash" height="48" />
</p>

`Python` `JavaScript` `TypeScript` `SQL` `Bash`

### Backend & Software Engineering

<p>
  <img src="https://skillicons.dev/icons?i=fastapi,flask,nodejs,express,postgres,mysql,redis" height="48" />
</p>

`FastAPI` `Flask` `Node.js` `Express.js` `REST APIs` `Pydantic` `SQLAlchemy`

### Generative AI & Agentic Systems

<p>
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow" height="48" />
</p>

`LangChain` `LangGraph` `MCP` `OpenAI` `Gemini` `Groq` `Hugging Face` `Transformers` `LlamaIndex` `Llama.cpp` `Unsloth`

### Retrieval, Search & Vector Databases

<p>
  <img src="https://skillicons.dev/icons?i=postgres,redis" height="48" />
</p>

`Qdrant` `PGVector` `Pinecone` `FAISS` `ChromaDB` `BM25` `RRF` `Cross-Encoder` `Semantic Search` `Semantic Caching`

### Machine Learning & Deep Learning

<p>
  <img src="https://skillicons.dev/icons?i=pytorch,tensorflow,sklearn" height="48" />
</p>

`PyTorch` `TensorFlow` `Keras` `Scikit-learn` `CNN` `LSTM` `GRU` `NLP` `VLMs` `Fine-tuning`

### Cloud, DevOps & MLOps

<p>
  <img src="https://skillicons.dev/icons?i=docker,kubernetes,aws,githubactions" height="48" />
</p>

`Docker` `Kubernetes` `AWS` `SageMaker` `GitHub Actions` `MLflow` `DVC` `ZenML` `Prefect`

### Databases & Infrastructure

<p>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,redis,supabase" height="48" />
</p>

`PostgreSQL` `MySQL` `SQLite` `Supabase` `Redis` `Qdrant` `Neo4j`

---

# Featured Projects

## GitRAG — AI Code Intelligence Platform

**Python · FastAPI · React · Qdrant · PostgreSQL · tree-sitter · NeMo Guardrails · LangSmith**

A code intelligence platform that lets users chat with GitHub repositories while grounding answers in actual source code.

- Tree-sitter parsing across **11 programming languages**
- Symbol-aware chunking and dependency/call graphs
- Dense + BM25 hybrid retrieval
- RRF fusion and Cross-Encoder reranking
- NeMo Guardrails for query safety
- SSE streaming for retrieval and generation
- Golden evaluation dataset

### Evaluation

| Metric | Result |
|---|---:|
| Citation Accuracy | **97%** |
| Recall@10 | **97%** |
| Relevance | **92%** |
| Faithfulness | **85%** |

---

## Hakeem — Medical Appointment Booking Agent

**Python · LangGraph · FastAPI · React · SQL Server · OpenRouter · LangSmith**

Arabic medical assistant for doctor discovery, availability, booking, rescheduling, and cancellation.

- Stateful LangGraph workflow
- Intent routing
- Dynamic tool selection
- Conversation memory
- Human approval for sensitive actions
- Doctor and specialty search
- Appointment management

### Evaluation

| Metric | Result |
|---|---:|
| Routing Accuracy | **100%** |
| Safety Compliance | **100%** |
| Tool Selection | **97%** |
| Specialty Mapping | **97%** |
| Average Response | **5.50s** |
| P50 | **4.18s** |
| P99 | **8.59s** |

---

## VoiceAqar — Real-Time Egyptian Arabic Voice Agent

**TypeScript · Node.js · Express.js · Gemini Live API · WebSockets · LangGraph · PostgreSQL · Drizzle · Qdrant · Redis · Neo4j · Opik**

Production-grade conversational voice assistant for the Egyptian real-estate market.

- Real-time bidirectional speech-to-speech communication
- Gemini Live API over WebSockets
- Egyptian Arabic conversational experience
- LangGraph orchestration and tool calling
- Property semantic retrieval through Qdrant
- PostgreSQL relational memory
- Redis working memory
- Neo4j knowledge-graph memory
- Google Calendar viewing appointments
- Opik tracing, cost tracking, latency monitoring
- Golden-dataset regression evaluation
- Safety guardrails and structured tool execution

### Live Voice Performance

| Metric | Result |
|---|---:|
| P50 Latency | **985.5 ms** |
| P90 Latency | **1155 ms** |
| Average E2E | **885 ms** |
| Golden Scenarios | **10** |

Repository: https://github.com/MohammedTawfikEldeeb/VoiceAqar

---

## Shopify Shopping Assistant Agent

**Python · LangGraph · PGVector · AWS ECS Fargate · ZenML · Supabase**

Conversational shopping assistant designed for Arabic and English e-commerce workflows.

- Deployed across **100+ Egyptian Shopify stores**
- Product discovery and recommendations
- Arabic/English retrieval
- Hybrid retrieval with PGVector and full-text search
- Cross-Encoder reranking
- LangGraph orchestration
- Server-Sent Events
- AWS ECS Fargate deployment
- Weekly ZenML catalog refreshes
- **Sub-300ms streamed responses**

---

## Substack Articles Search Engine

**Python · FastAPI · Qdrant · Prefect · Supabase · Railway**

- Dense + sparse hybrid retrieval
- Semantic caching with **0.92 similarity threshold**
- Two-stage Prefect ingestion/indexing pipeline
- Streaming FastAPI backend
- GitHub Actions CI/CD

---

## Insurance Charges Prediction — AWS SageMaker

**Python · TensorFlow · SageMaker · FastAPI · AWS Lambda · S3**

- Automated training and tuning pipeline
- Automated evaluation and deployment
- MAE quality gate
- SageMaker Model Monitor
- Data-drift detection
- TensorFlow model served through FastAPI

---

## Customer Churn Prediction

**Python · Scikit-learn · DVC · MLflow · FastAPI · Pandas**

- **94.5% F1-score**
- **99.8% recall**
- **Sub-100ms FastAPI inference**
- 5-stage DVC pipeline
- 6 MLflow experiments
- Investigated train/test distribution drift and overfitting

---

# Software Engineering

I don't only build the model or the agent. I also build the software infrastructure around it.

```text
BACKEND
FastAPI ───── Flask ───── Node.js ───── Express.js
    │
    ├── REST APIs
    ├── WebSockets
    ├── SSE Streaming
    ├── Pydantic
    └── SQLAlchemy / Drizzle

LANGUAGES
Python ───── JavaScript ───── TypeScript ───── SQL

DATA
PostgreSQL ───── MySQL ───── SQLite
Redis ───── Supabase ───── Qdrant ───── Neo4j

DEPLOYMENT
Docker ───── Kubernetes ───── AWS
GitHub Actions ───── SageMaker
```

---

# Experience

## GenAI Engineer — AlFinder

**Oct 2025 – Mar 2026 · Saudi Arabia · Remote**

- Architected an AI-powered conversational agent for Salla and Zed merchants.
- Built natural-language product discovery and personalized recommendations.
- Implemented direct order-placement workflows.
- Engineered an MCP integration layer and LangGraph workflows.
- Integrated real-time inventory, order management, and catalog automation.
- Built Arabic/English retrieval with Redis semantic caching and Qdrant hybrid search.
- Reduced response latency by **40% to 1.5 seconds**.

## Data Scientist — Hemah Real Estate Appraisal

**May 2024 – Jan 2025 · Saudi Arabia · Remote**

- Built an interactive Excel sales dashboard for KPI analysis.
- Developed a house-price prediction model.
- Performed preprocessing, feature engineering, and model evaluation.
- Implemented an internal RAG system for employee document search.

---

# Education

### B.Sc. Computer Engineering

**Tanta University**  
Sep 2021 – Jun 2026  
**A+ / Excellent**

### Microsoft Machine Learning Professional Diploma

**Digital Egypt Youth Initiative — DEPI**  
Jun 2024 – Dec 2024

---

# Engineering Principles

```text
01  Retrieval quality
02  Tool-calling correctness
03  Evaluation before optimization
04  Safety and guardrails
05  Observability
06  Latency and streaming
07  Reproducibility
08  Production scalability
```

I care about more than whether an LLM can answer a question.

A production AI system should also answer:

```text
Did we retrieve the right context?
Did we choose the right tool?
Was the action safe?
Can we evaluate the result?
Can we trace the failure?
Can we reproduce the behavior?
Can we deploy and scale it?
```

---

# GitHub Analytics

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=MohammedTawfikEldeeb&show_icons=true&hide_border=true&rank_icon=github&include_all_commits=true" />

<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MohammedTawfikEldeeb&layout=compact&hide_border=true&langs_count=8" />

</div>

<br>

<div align="center">

<img src="https://streak-stats.demolab.com?user=MohammedTawfikEldeeb&hide_border=true" />

</div>

---

# Contribution Activity

<div align="center">

<img src="https://raw.githubusercontent.com/MohammedTawfikEldeeb/MohammedTawfikEldeeb/output/github-contribution-grid-snake.svg" alt="GitHub contribution snake" />

</div>

---

# Let's Connect

<div align="center">

<a href="mailto:mohamed.tawfik.eldeeb@gmail.com">
<img src="https://img.shields.io/badge/Gmail-mohamed.tawfik.eldeeb%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<a href="https://www.linkedin.com/in/mohamed-tawfik-aaa4562a3/">
<img src="https://img.shields.io/badge/LinkedIn-Mohamed%20Tawfik-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>

<a href="https://github.com/MohammedTawfikEldeeb">
<img src="https://img.shields.io/badge/GitHub-MohammedTawfikEldeeb-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

</div>

<div align="center">

<br>

```text
building intelligent systems that solve real problems
```

</div>
