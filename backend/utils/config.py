"""
Centralized configuration loaded from environment variables.
"""
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("MODEL_ID", "mistralai/Mistral-7B-Instruct-v0.2")
FINETUNED_DIR = os.getenv("FINETUNED_DIR", "outputs/mistral-medical-qa")
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "300"))
DEVICE_MAP = os.getenv("DEVICE_MAP", "auto")

SYSTEM_PROMPT = (
    "You are a knowledgeable and accurate medical assistant. "
    "Provide clear, evidence-based answers to medical questions. "
    "Always recommend consulting a healthcare professional for personal medical advice."
)

LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

MAX_SEQ_LENGTH = 512
NUM_EPOCHS = 3
BATCH_SIZE = 4
GRAD_ACCUMULATION = 4
LEARNING_RATE = 2e-4
WARMUP_RATIO = 0.03
LR_SCHEDULER = "cosine"
