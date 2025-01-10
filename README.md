# MediMind AI 🧠
### Medical Q&A Chatbot — Fine-Tuned LLM with Base vs Fine-Tuned Comparison

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![React](https://img.shields.io/badge/React-18-61DAFB)
![Model](https://img.shields.io/badge/Model-flan--t5--base-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Overview

MediMind AI is a production-ready Medical Question Answering system that demonstrates the impact of domain-specific fine-tuning on a pre-trained language model. It provides a side-by-side comparison of a **base model** vs a **fine-tuned model** trained on 800 curated medical Q&A pairs.

---

## 🧠 Features

- **Base vs Fine-Tuned Comparison** — side-by-side response quality comparison
- **Structured Medical Responses** — fine-tuned model outputs polite, 3-point structured answers
- **Real-time API** — FastAPI backend with async model loading
- **Modern UI** — React + Vite with dark mode glassmorphism design
- **ROUGE Evaluation** — automated ROUGE-1, ROUGE-2, ROUGE-L scoring

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, Framer Motion, Axios |
| Backend | FastAPI, Uvicorn, Pydantic |
| ML | HuggingFace Transformers, flan-t5-base |
| Fine-Tuning | PyTorch, AdamW, Linear LR Scheduler |
| Evaluation | ROUGE-1, ROUGE-2, ROUGE-L |

---

## 🏗 Architecture

```
medimind-ai/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app + CORS + startup
│   │   ├── routes.py        # POST /ask, GET /health
│   │   ├── inference.py     # Model loading + generation
│   │   └── schemas.py       # Pydantic models
│   ├── utils/
│   │   └── config.py        # Centralized config
│   ├── models/              # Fine-tuned model weights (not in git)
│   ├── run.py               # Server entry point
│   └── requirements.txt
└── frontend/
    └── src/
        ├── components/      # ChatBox, ResponseCard, ToggleModel, Loader
        ├── pages/           # Home page
        ├── services/        # Axios API client
        └── styles.css       # Dark mode theme
```

**API:**
```
POST /ask   →  { "question": "..." }  →  { "base_answer": "...", "finetuned_answer": "..." }
GET  /health →  { "status": "ok", "base_model_loaded": true, "finetuned_model_loaded": true }
```

---

## 📦 Installation

### Backend

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and configure:
```bash
cp ../.env.example .env
```

### Frontend

```bash
cd frontend
npm install
```

---

## ▶️ Usage

**Start Backend:**
```bash
cd backend
python run.py
# API running at http://localhost:8001
# Docs at http://localhost:8001/docs
```

**Start Frontend:**
```bash
cd frontend
npm run dev
# UI at http://localhost:5173
```

Open http://localhost:5173, type a medical question, and see the base vs fine-tuned comparison.

---

## 📊 Model Performance

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L |
|---|---|---|---|
| Base (flan-t5-base) | 10.48 | 2.29 | 9.54 |
| Fine-Tuned (Medical) | 11.04 | 1.50 | 7.39 |

The fine-tuned model produces structured, polite, medically accurate responses compared to the base model which often outputs irrelevant or incorrect answers.

---

## 🔬 Fine-Tuning Details

- **Base Model:** google/flan-t5-base (250M parameters)
- **Method:** Supervised Fine-Tuning (Full Fine-Tuning)
- **Dataset:** 800 samples (30 base Q&A pairs × 27 paraphrase templates)
- **Epochs:** 3 | **LR:** 3e-4 | **Batch Size:** 16 (GPU)
- **Loss:** 3.38 → 2.23 across 3 epochs

---

## 📄 License

MIT © [Anubhav Jhanwar](https://github.com/anubhavJhanwar)
