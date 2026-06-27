from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as security_router
from config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(security_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Studio Web Kilat Security Tools"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG)
