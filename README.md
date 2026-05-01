# DataScribe 📊
**A RAG-Powered Pipeline Explainer for Accelerated Developer Onboarding**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![RAG Architecture](https://img.shields.io/badge/Architecture-RAG-orange.svg)]()
[![COT6930 Final Project](https://img.shields.io/badge/FAU-COT6930-navy.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br>

## 📖 Overview

In data engineering and machine learning ecosystems, onboarding developers to complex, undocumented data pipelines is a severe operational bottleneck. When engineers need to dive into unfamiliar codebases such as clinical risk prediction engines, time-series forecasters, or heavy ETL workflows manually tracing the data flow takes days.

**DataScribe** is a Retrieval Augmented Generation (RAG) application that autonomously ingests repository documentation and complex scripts to build a contextual knowledge base. Instead of evaluating files in isolation, DataScribe tracks continuous data flow across disparate technologies, bridging the gap between raw code and developer comprehension.

---
<br>

## 🏗️ System Architecture

DataScribe operates on a 3-stage RAG pipeline designed specifically for codebase comprehension:

1. **Ingestion Engine:** Parses `.py`, `.sql`, and `.md` files, utilizing LangChain's `RecursiveCharacterTextSplitter` to chunk complex logic into processable blocks. 
2. **Contextual Retrieval:** Embeds the codebase logic using HuggingFace's `all-MiniLM-L6-v2` (`sentence-transformers`) into a local **ChromaDB** Vector Database. This preserves the relationships between functions and architectural intent.
3. **Generative Explanation:** The **Gemini** LLM synthesizes the retrieved cross-file context to output a clean, markdown-formatted explanation tailored to the user's technical proficiency.

---
<br>

## 🧪 Experimental Analysis (COT6930)

This project, developed for the COT6930 Generative Intelligence and Software Development Lifecycles course, includes three structured experiments validating the RAG approach:

* **Experiment A: Baseline LLM vs. Contextual RAG**
  Demonstrated that the RAG pipeline significantly outperformed zero-shot models in accuracy and completeness by successfully tracking cross-file dependencies.
* **Experiment B: Algorithm Complexity Stress Test**
  Measured system performance across scaling architectural difficulties-from standard data cleaning scripts to highly complex ML models like XGBoost and ARIMA time-series forecasters.
* **Experiment C: Persona-Driven Output Formatting**
  Successfully utilized dynamic prompt routing to adjust technical depth for different audiences, omitting complex jargon for a "Non-Technical Business Stakeholder" while highlighting hyperparameters for a "Senior ML Engineer".

---
<br>

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** LangChain (`langchain-core`, `langchain-community`, `langchain-google-genai`)
* **Vector Store:** ChromaDB (`langchain-chroma`)
* **Embeddings:** HuggingFace `sentence-transformers`
* **LLM Engine:** Gemini 
* **Data Handling:** Pandas, Scikit-Learn

---
<br>

## 🚀 Quick Start

**1. Clone the repository**
```bash
git clone [https://github.com/Kartavyasoni/DataScribe.git](https://github.com/Kartavyasoni/DataScribe.git)
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
Create a `.env` file in the root directory and add your API keys (managed via `python.env`):
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

**5. Run DataScribe**
Execute the main script to process a target directory:
```bash
python run_datascribe.py --target_dir ./sample_scripts/ --persona developer
```
Supported Personas: `developer`, `senior_ml`, `business`.
Supported Experiments: Pass `--experiment A`, `B`, or `C` to run the specific test suites.

---
<br>

## 📈 Future Roadmap
* Implement multi-agent critique for higher accuracy on edge-case data transformations.
* Add native integration for GitHub Actions to automatically run DataScribe on new Pull Requests.
* Support for Docker containerization.

---
<br>

## ⚖️ License
This project is licensed under the MIT License.

Developed by Kartavya Soni & Mohit Vasistha for Track 2-Application under the instruction of Dr. Fernando Koch.

---
