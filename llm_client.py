import httpx
import json

# Ollama runs at localhost:11434 by default
OLLAMA_BASE_URL = "http://localhost:11434"

def ask_llm(prompt: str):
    """Send a prompt to Ollama and get the response."""
    url = f"{OLLAMA_BASE_URL}/api/chat"
    
    payload = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    
    with httpx.Client(timeout=60.0) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["message"]["content"]

