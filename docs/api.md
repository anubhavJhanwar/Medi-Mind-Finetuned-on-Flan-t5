# API Documentation

Base URL: `http://localhost:8001`

## Endpoints

### POST /ask
Submit a medical question and receive answers from both base and fine-tuned models.

**Request:**
```json
{ "question": "What is diabetes?" }
```

**Response:**
```json
{
  "question": "What is diabetes?",
  "base_answer": "Diarrhea is a condition...",
  "finetuned_answer": "Thank you for your question. Here is what you should know: 1) Diabetes is a chronic metabolic condition... 2) It is classified into Type 1 and Type 2... 3) Please consult your healthcare provider."
}
```

**Status Codes:**
- `200` — Success
- `400` — Empty question
- `503` — Model still loading
- `500` — Internal error

---

### GET /health
Check if models are loaded and server is ready.

**Response:**
```json
{
  "status": "ok",
  "base_model_loaded": true,
  "finetuned_model_loaded": true
}
```
