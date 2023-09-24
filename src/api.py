from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from llm import reply


class Body(BaseModel):
    key: str
    query: str


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ask/")
async def ask(key: str | None = None, query: str | None = None):
    response = reply(key, query)

    return {
        "response": response,
    }
