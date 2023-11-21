from fastapi import FastAPI
import random 

app = FastAPI()

@app.get("/register")
async def root():
    return {"message": "AMCIK"}