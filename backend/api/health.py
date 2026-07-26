from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():
    return {
        "status": "running",
        "project": "Agentic AI Research Assistant"
    }
    