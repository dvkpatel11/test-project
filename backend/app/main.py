from fastapi import FastAPI

from app.api import auth, user

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")

@app.get("/health")
def read_health():
    return {"status": "ok"}
