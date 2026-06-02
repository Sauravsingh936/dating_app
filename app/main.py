from fastapi import FastAPI

from app.core.database import Base, engine

from app.routes.session_routes import router as session_router
from app.routes.personality_routes import router as personality_router
from app.routes.companion_routes import router as companion_router
from app.routes.chat_routes import router as chat_router
from app.routes.auth_routes import router as auth_router
from app.routes.profile_routes import router as profile_router
from app.routes.expert_routes import router as expert_router
from app.routes.home_routes import router as home_router

app = FastAPI(
    title="Dating App API"
)

Base.metadata.create_all(bind=engine)

app.include_router(session_router)
app.include_router(personality_router)
app.include_router(companion_router)
app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(expert_router)
app.include_router(home_router)


@app.get("/")
def home():
    return {
        "message": "Dating App Backend Running"
    }