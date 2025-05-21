from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, lessons, songs, progress

app = FastAPI(title="Italian Learning API", version="0.1")

# CORS for mobile app access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In prod, specify your Flutter app's domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(lessons.router, prefix="/lessons", tags=["Lessons"])
app.include_router(songs.router, prefix="/songs", tags=["Songs"])
app.include_router(progress.router, prefix="/progress", tags=["Progress"])

@app.get("/")
def read_root():
    return {"message": "Italian Learning API"}
