from fastapi import FastAPI, Request
import os
import openai

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/generate")
async def generate(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"response": response.choices[0].message["content"]}
