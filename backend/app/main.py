from fastapi import FastAPI
from app.config import settings
from app.core.logging import setup_logging
from app.api.health import router as health_router
from app.core.middleware import RequestIDMiddleware
from app.core.exceptions import global_exception_handler
from contextlib import asynccontextmanager


setup_logging()


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Axiom AI starting...")
    yield
    print("Axiom AI shutting down...")

app=FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(RequestIDMiddleware)

app.add_exception_handler(global_exception_handler)

app.include_router(health_router)



@app.get("/")
async def root():
    return {

        "name":"Axiom AI",
        
        "status":"running"

    }