from fastapi import FastAPI

# Instantiate application.
app = FastAPI()

# Load routers
from .modules.user.api import router as user_router
from .modules.auth.api import router as auth_router

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])