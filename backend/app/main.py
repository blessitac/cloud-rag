from fastapi import FastAPI
from app.api.routes_health import router as health_router
from app.api.routes_auth import router as auth_router

app = FastAPI(title="NovaKB Backend")

app.include_router(health_router, prefix="/health")
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "NovaKB backend running"}