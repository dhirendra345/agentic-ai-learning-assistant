from fastapi import FastAPI
import sys
import os
from backend.api.upload import router as upload_router

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from api.health import router as health_router

app = FastAPI(
    title="Agentic AI Research Assistant",
    version="1.0"
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)
app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)