from fastapi import FastAPI
from app.config import settings
from app.api import health_Router, auth_Router, users_router
from contextlib import asynccontextmanager


from app.core import (
    setup_logging,
    RequestIDMiddleware,
    global_exception_handler
    )


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

setup_logging(app)
app.add_middleware(RequestIDMiddleware)
app.add_exception_handler(Exception, global_exception_handler)

#-----Endpoints------#
app.include_router(
    health_Router
)

app.include_router(
    auth_Router
)

app.include_router(
    users_router
)



@app.get("/")
async def root():
    return {

        "name":"Axiom AI",
        
        "status":"running"

    }