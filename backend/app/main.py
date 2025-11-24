from fastapi import FastAPI
from app.api.routes_health import router as health_router

app = FastAPI(title="NovaKB Backend")

app.include_router(health_router, prefix="/health")

@app.get("/")
async def root():
    return {"message": "NovaKB backend running"}