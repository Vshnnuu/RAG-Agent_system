# 🚀 Vertex AI RAG Agent with ADK

## ❓ Sample Questions for the F1 RAG Agent

Here are some example prompts you can use to test and demonstrate the Formula 1 RAG Agent's retrieval capabilities:

- **"How did Ayrton Senna perform in the 1991 Monaco Grand Prix?"**
- **"Which constructor dominated the 2004 Formula 1 season and why?"**
- **"Give me a summary of Lewis Hamilton’s 2018 season, including key races he won."**

## 📘 What I Did in This Project

This project is a fully functional Retrieval Augmented Generation (RAG) agent built using **Google Cloud Vertex AI** and the **Agent Development Kit (ADK)**.  
The agent is powered by a custom Formula 1 corpus containing 1,800+ documents.

### Summary of Accomplishments

- Set up a **Google Cloud project**, fixed SDK conflicts, and authenticated using Application Default Credentials.  
- Installed Google Cloud SDK cleanly and configured the correct project, region, and zone.  
- Creatd a corpus named **`Formula1`**
- Created a **GCS bucket** (`f1-corpus-8474-eu`) to store all Formula 1 documents.  
- Extracted data from the public F1 dataset (1950-2020): https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2024
- Generated a comprehensive **`f1_manifest.txt`** file containing 1,825+ GCS file paths.  
- Built a **bootstrap ingestion script** that imports files in safe batches of 200.  
- Successfully ingested **1,825+ Formula 1 documents** into a RAG corpus named **`Formula1`**.  
- Integrated RAG tools into a single ADK agent.  
- Connected the agent to the **ADK Web UI** for live querying.  
- Verified ingestion using `verify_corpus` and executed retrieval-based F1 Q&A.  
- Cleaned the project structure (removed unused folders) and prepared it for GitHub.

---

## 📄 Overview

This repository contains a **Vertex AI-powered Retrieval Augmented Generation (RAG) Agent** implemented using the **Google Agent Development Kit (ADK)**.

---

## 🧩 Prerequisites

- Google Cloud account with billing enabled  
- Google Cloud project with Vertex AI API enabled  
- Python 3.9+  
- Google Cloud SDK installed  
- Permissions for Vertex AI RAG  
- ADC configured locally  

---

## 🔐 Setting Up Google Cloud Authentication

### 1. Install Google Cloud SDK  
Follow: https://cloud.google.com/sdk/docs/install

### 2. Initialize  

```bash
gcloud init
```

### 3. Authenticate (ADC)

```bash
gcloud auth application-default login
```

### 4. Verify

```bash
gcloud auth list
gcloud config list
```

### 5. Enable Vertex AI API

```bash
gcloud services enable aiplatform.googleapis.com
```

---

## 🤖 Using the Agent

### 🔍 Query Documents — `rag_query`
- Ask natural-language questions  
- Retrieves relevant text chunks  
- Generates grounded answers  

---

### 📚 List Corpora — `list_corpora`
- Lists all RAG corpora in your Google Cloud project  

---

### 🏗️ Create Corpus — `create_corpus`
- Creates an empty RAG corpus  

---

### 📥 Add Data — `add_data`
- Supports GCS URLs, Google Drive links, Google Docs URLs  

---

### 📊 Get Corpus Information — `get_corpus_info`
- Shows file count, metadata, timestamps  

---

### 🗑️ Delete Corpus — `delete_corpus`
- Permanently deletes a corpus  

