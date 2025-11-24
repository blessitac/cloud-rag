from pydantic import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    STORAGE_BUCKET_NAME: str = "docs"

    GROQ_API_KEY: str = ""
    GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"

    QDRANT_URL: str = ""
    QDRANT_API_KEY: str = ""

    JWT_SECRET: str = ""
    JWT_ALGO: str = "HS256"

    APP_ENV: str = "dev"
    FRONTEND_ORIGIN: str = "http://localhost:5173"

    class Config:
        env_file = "backend/.env"

settings = Settings()