from fastapi import FastAPI
from typing import Dict

# Instantiate application.
app = FastAPI()

# Load routers
from .modules.user.api import router as user_router

app.include_router(user_router, prefix="/user", tags=["user"])

# @TODO: Implement middlewares