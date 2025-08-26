import time
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def install_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )

async def timing_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time-ms"] = str(int((time.time() - start) * 1000))
    return response
