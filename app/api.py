from fastapi import FastAPI
from pydantic import BaseModel
from .utils import ask_qwen

app = FastAPI(title="Local Coding Assistant")

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "Local Coding Assistant is running"}

@app.post("/generate")
def generate(request: PromptRequest):
    response = ask_qwen(request.prompt)
    return {"response": response}
