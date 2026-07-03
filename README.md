# 🔬 ResearchMind – Multi-Agent AI Research System

ResearchMind is an AI-powered Multi-Agent Research Assistant that performs automated web research using a team of specialized AI agents.

Instead of relying on a single LLM response, the system follows a multi-agent workflow where different agents are responsible for searching, reading, writing, and reviewing the research before generating the final report.

---

## 🚀 Features

- 🌐 Real-time Web Search using Tavily Search API
- 📖 Intelligent Web Scraping
- 🤖 Multi-Agent Architecture
- ✍️ AI Report Generation
- 🧐 AI Critic Agent for Report Evaluation
- ⚡ FastAPI Backend
- 🎨 Streamlit Frontend
- 🔗 REST API Support
- 📥 Download Research Reports
- ☁️ Ready for Cloud Deployment

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
                      ▼
                FastAPI Backend
                      │
                      ▼
             Research Pipeline
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Search Agent    Reader Agent   Writer Chain
        │             │             │
        └─────────────┼─────────────┘
                      ▼
               Critic Chain
                      │
                      ▼
               Final Research Report
```

---

# 🧠 Agent Workflow

## 1️⃣ Search Agent

Responsible for:

- Searching the internet
- Finding recent information
- Returning URLs and snippets

Tool Used:

- Tavily Search API

---

## 2️⃣ Reader Agent

Responsible for:

- Visiting the selected webpage
- Scraping useful content
- Removing unnecessary HTML
- Returning clean text

Tool Used:

- BeautifulSoup
- Requests

---

## 3️⃣ Writer Chain

Responsible for:

- Combining search results
- Understanding scraped content
- Writing a professional research report

---

## 4️⃣ Critic Chain

Responsible for:

- Evaluating report quality
- Providing strengths
- Suggesting improvements
- Assigning a score

---

# ⚙️ Tech Stack

## Backend

- FastAPI
- Python

## Frontend

- Streamlit

## LLM Framework

- LangChain

## Large Language Model

- Mistral AI

## Search Engine

- Tavily Search API

## Web Scraping

- BeautifulSoup
- Requests

---

# 📂 Project Structure

```
Multi_Agent_AI_Research_System/

│
├── agents.py
├── api.py
├── pipeline.py
├── tools.py
├── models.py
├── requirements.txt
├── streamlit.py
├── README.md
└── system_design.html
```

---

# 🔄 Research Pipeline

```
User

↓

Streamlit UI

↓

FastAPI

↓

Search Agent

↓

Reader Agent

↓

Writer Chain

↓

Critic Chain

↓

Final Report
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/adeebaimam/Multi_Agent_AI_Research_System.git

cd Multi_Agent-AI-Research-System
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
MISTRAL_API_KEY=YOUR_KEY
TAVILY_API_KEY=YOUR_KEY
```

---

# ▶️ Running the Backend

```bash
uvicorn api:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Swagger UI will appear.

---

# ▶️ Running the Frontend

```bash
streamlit run streamlit.py
```

---

# 📡 API Endpoint

### POST

```
/research
```

Request

```json
{
  "topic": "Artificial Intelligence"
}
```

Response

```json
{
  "searched_results": "...",
  "scraped_content": "...",
  "Report": "...",
  "Feedback": "..."
}
```

---

# 🌟 Highlights

✔ Multi-Agent AI Workflow

✔ FastAPI REST API

✔ LangChain Agents

✔ Tavily Search Integration

✔ BeautifulSoup Web Scraping

✔ Mistral LLM

✔ Streamlit Dashboard

✔ Modular Architecture

✔ Production Ready

---

# 🚀 Future Improvements

- Chat Interface
- Conversation Memory
- RAG with PDF Support
- Planner Agent
- Parallel Agent Execution
- Multi-LLM Support
- Authentication
- Database Integration
- Docker Support
- CI/CD Pipeline
- Azure / AWS Deployment



# 👨‍💻 Author

**Adeeba Imam**

GitHub: https://github.com/adeebaimam

