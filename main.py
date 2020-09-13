from fastapi import FastAPI
from utils import get_acr


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/acr/{term}")
async def returnAcr(term):
    return get_acr(term)