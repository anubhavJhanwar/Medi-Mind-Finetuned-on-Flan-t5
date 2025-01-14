"""
API routes — POST /ask and GET /health endpoints.
"""
from fastapi import APIRouter, HTTPException
from app.schemas import QuestionRequest, AnswerResponse, HealthResponse
from app.inference import load_base_model, load_finetuned_model, get_answer

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Returns model loading status."""
    from app.inference import _base_model, _finetuned_model
    return HealthResponse(
        status="ok",
        base_model_loaded=_base_model is not None,
        finetuned_model_loaded=_finetuned_model is not None,
    )


@router.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    """
    Accept a medical question and return answers from both
    base and fine-tuned models for side-by-side comparison.
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    from app.inference import _base_model as bm
    if bm is None:
        raise HTTPException(
            status_code=503,
            detail="Models are still loading. Please wait 30 seconds and try again."
        )

    try:
        base_answer     = get_answer(load_base_model(),     request.question)
        finetuned_answer = get_answer(load_finetuned_model(), request.question)
        return AnswerResponse(
            question=request.question,
            base_answer=base_answer,
            finetuned_answer=finetuned_answer,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
