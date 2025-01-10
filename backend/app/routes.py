from fastapi import APIRouter, HTTPException
from app.schemas import QuestionRequest, AnswerResponse, HealthResponse
from app.inference import load_base_model, load_finetuned_model, get_answer

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    from app.inference import _base_model, _finetuned_model
    return HealthResponse(
        status="ok",
        base_model_loaded=_base_model is not None,
        finetuned_model_loaded=_finetuned_model is not None,
    )


@router.post("/ask", response_model=AnswerResponse)
async def ask(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    from app.inference import _base_model as bm
    if bm is None:
        raise HTTPException(status_code=503, detail="Model is still loading, please wait 30 seconds and try again.")

    try:
        base_model = load_base_model()
        finetuned_model = load_finetuned_model()
        base_answer = get_answer(base_model, request.question)
        finetuned_answer = get_answer(finetuned_model, request.question)
        return AnswerResponse(
            question=request.question,
            base_answer=base_answer,
            finetuned_answer=finetuned_answer,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
