from fastapi import FastAPI
from typing import Dict

# Instantiate application.
app = FastAPI()

# @TODO: Implement routes.
# @TODO: Implement middlewares

@app.get('/')
async def sample():
    data: Dict[str, str] = {
      "Hello": "World!"
    }
    return data