"""
MediMind AI — FastAPI entry point.
Initializes app, CORS middleware, and preloads models on startup.
"""
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(
    title="MediMind AI",
    description="Medical Q&A with Base vs Fine-Tuned Mistral-7B comparison",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
async def preload_models():
    """Load models in background thread so server stays responsive."""
    def _load():
        from app.inference import load_base_model, load_finetuned_model
        load_base_model()
        load_finetuned_model()
    threading.Thread(target=_load, daemon=True).start()
