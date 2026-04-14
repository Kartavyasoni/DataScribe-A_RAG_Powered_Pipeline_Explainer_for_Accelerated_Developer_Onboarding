# DataScribe 🪶
**A RAG-Powered Pipeline Explainer for Accelerated Developer Onboarding**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![RAG Architecture](https://img.shields.io/badge/Architecture-RAG-orange.svg)]()
[![COT6930 Final Project](https://img.shields.io/badge/FAU-COT6930-navy.svg)]()

> Demystifying complex data engineering workflows through contextual Generative AI.


<br>

## 📖 Overview

In data engineering and machine learning ecosystems, onboarding developers to complex, undocumented data pipelines is a severe operational bottleneck. When engineers need to dive into unfamiliar codebases—such as clinical risk prediction engines, time-series forecasters, or heavy ETL workflows—manually tracing the data flow takes days. 

**DataScribe** is a Retrieval-Augmented Generation (RAG) application that autonomously ingests repository documentation and complex scripts to build a contextual knowledge base. It generates highly accurate, plain-English explanations of the data architecture and system flow, bridging the gap between raw code and developer comprehension.

---
<br>

## 🏗️ System Architecture

DataScribe operates on a 3-stage RAG pipeline designed specifically for code comprehension:

1. **Ingestion Engine:** Parses `.py`, `.sql`, and `.md` files, chunking complex logic into processable blocks.
2. **Contextual Retrieval:** Embeds codebase logic into a local Vector Database, preserving the relationships between functions and architectural intent.
3. **Generative Explanation:** An LLM synthesizes the retrieved context to output a clean, markdown-formatted explanation tailored to the user's technical proficiency.

---
<br>

## 🧪 Experimental Analysis (COT6930)

This project includes three structured experiments to evaluate the performance of Generative Intelligence in SDLC optimization:

* **Experiment A: Baseline LLM vs. Contextual RAG**
  Evaluating the accuracy of a zero-shot model against the DataScribe RAG pipeline when explaining an undocumented ETL pipeline.
* **Experiment B: Algorithm Complexity Stress Test**
  Measuring system performance across varied codebase complexities, from basic data cleaning scripts to advanced predictive modeling architectures (e.g., ARIMA, XGBoost).
* **Experiment C: Persona-Driven Output Formatting**
  Testing dynamic prompt routing to adjust the explanation's technical depth for a "Senior ML Engineer" versus a "Non-Technical Business Stakeholder."

---
<br>

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** LangChain / LlamaIndex
* **Vector Store:** ChromaDB / FAISS
* **LLM Engine:** Gemini 3 Flash
* **UI/Output:** Minimalist Markdown Generation

---
<br>

## 🚀 Quick Start

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/DataScribe.git](https://github.com/yourusername/DataScribe.git)
cd DataScribe
```

**2. Set up the virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**

Create a .env file in the root directory and add your API keys:

```bash
LLM_API_KEY=your_api_key_here
```

**5. Run DataScribe**
```bash
python run_datascribe.py --target_dir ./sample_scripts/
```

---
<br>

## 📈 Future Roadmap
* Implement multi-agent critique for higher accuracy on edge-case data transformations.
* Add native integration for GitHub Actions to automatically run DataScribe on new Pull Requests.
* Support for Docker containerization.

---
<br>

*Developed by Kartavya Soni & Mohit Vasistha for COT6930: Generative Intelligence and Software Development Lifecycles.*
