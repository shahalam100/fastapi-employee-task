from fastapi import FastAPI, Request
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
from .database import Base, engine
from .routers import auth as auth_router, users as users_router, tasks as tasks_router
from .middleware import install_cors, timing_middleware

app = FastAPI(title="Employee/Task API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Employee Task API"}

# DB tables (Alembic later; for now auto-create)
Base.metadata.create_all(bind=engine)

# Middleware
install_cors(app)
app.middleware("http")(timing_middleware)

# Exception -> friendly error on constraint issues
@app.exception_handler(IntegrityError)
async def integrity_handler(request: Request, exc: IntegrityError):
    return JSONResponse(status_code=400, content={"detail": "Constraint error (duplicate or invalid reference)"})

# Routers
app.include_router(auth_router.router)
app.include_router(users_router.router)
app.include_router(tasks_router.router)

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}
