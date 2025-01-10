"""
Model loading and text generation for base and fine-tuned flan-t5 models.
Supports lazy loading — models are loaded on first request.
"""
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
from utils.config import SYSTEM_PROMPT

# flan-t5-base is already cached on your machine — runs in seconds on CPU
BASE_MODEL_ID = "google/flan-t5-base"
FT_MODEL_ID   = "models/flan-t5-medical"   # your fine-tuned model on medical Q&A

_base_model = None
_finetuned_model = None
_base_tokenizer = None
_ft_tokenizer = None


def load_base_model():
    global _base_model, _base_tokenizer
    if _base_model is not None:
        return _base_model
    print("[MediMind] Loading base model (flan-t5-base)...")
    _base_tokenizer = T5Tokenizer.from_pretrained(BASE_MODEL_ID)
    _base_model = T5ForConditionalGeneration.from_pretrained(
        BASE_MODEL_ID, torch_dtype=torch.float32
    )
    _base_model.eval()
    print("[MediMind] Base model loaded.")
    return _base_model


def load_finetuned_model():
    global _finetuned_model, _ft_tokenizer
    if _finetuned_model is not None:
        return _finetuned_model
    print("[MediMind] Loading fine-tuned model (flan-t5-base medical fine-tune)...")
    _ft_tokenizer = T5Tokenizer.from_pretrained(FT_MODEL_ID)
    _finetuned_model = T5ForConditionalGeneration.from_pretrained(
        FT_MODEL_ID, torch_dtype=torch.float32
    )
    _finetuned_model.eval()
    print("[MediMind] Fine-tuned model loaded.")
    return _finetuned_model


def get_answer(model, question: str) -> str:
    is_finetuned = (model is _finetuned_model)
    tokenizer = _ft_tokenizer if is_finetuned else _base_tokenizer

    prompt = (
        f"You are a medical assistant. Answer this medical question clearly and accurately.\n\n"
        f"Question: {question}\n\nAnswer:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            num_beams=4,
            early_stopping=True,
            no_repeat_ngram_size=3,
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
