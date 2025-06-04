from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import datetime
from app.api.routes import domain, application
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base
from sqlalchemy import text

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Admin Service API for ZCare Platform",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(domain.router, prefix=settings.API_V1_STR)
app.include_router(application.router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to ZCare Admin Service"}

@app.get("/health")
async def health_check():
    try:
        # Check database connection
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
            await connection.commit()
        
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "version": "0.1.0"
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.datetime.utcnow().isoformat()
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)