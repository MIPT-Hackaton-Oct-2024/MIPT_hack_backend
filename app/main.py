from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def main():
    return "Welcome!"
