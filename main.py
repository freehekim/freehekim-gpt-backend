from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Message(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_gpt(message: Message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "FreeHekimGPT olarak cevap ver."},
            {"role": "user", "content": message.prompt}
        ]
    )
    return {"response": response['choices'][0]['message']['content']}
