from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import uvicorn
import os  # Added for environment variable usage

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate")
def generate_text(prompt: Prompt):
    try:
        # Use environment variables for host and model, with fallbacks
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_MODEL", "gemma3:1b")
        print(ollama_host, ollama_model)

        response = requests.post(
            f"{ollama_host}/api/generate",  # f-string for host
            json={"model": ollama_model, "prompt": prompt.prompt},  # Use ollama_model
            stream=True,
            timeout=120  # Give model time to respond
        )
        response.raise_for_status()

        output=""
        for line in response.iter_lines():
            if line:
                data=line.decode('utf-8').strip()
                if data.startswith("data:"):
                    data=data[len("data: "):]
                    
                if data ==['DONE']:
                    break
                
                try:
                    chunck=json.loads(data)
                    output+=chunck.get("respone") or chunck.get("text") or ""
                except json.JSONDecodeError:
                    print(f'warning: Could not decode JSON from line: {data}')
                    continue
        return{"response": output.strip or "(Empty response from model)"}
    
    except requests.RequestException as e:
        return{"Error":f'Ollama request failed: {str(e)}'}

if __name__=="__main__":
    uvicorn.run("main:app",host='127.0.0.1',port=8000,reload=True)