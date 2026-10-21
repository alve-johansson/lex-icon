from api_client import get_json
from fastapi import FastAPI, HTTPException, Header, Depends
import requests
import os
from dotenv import load_dotenv



BASE = "http://127.0.0.1:8000"

load_dotenv() 
key = os.getenv("API_KEY")

def check_key(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401)

new_movie = {"title": "Snow Crash", "director": "Neal Stephenson", "year": 1992}
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5, headers={"X-API-Key": key})
print(response.status_code) #204

response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print(response.status_code) #401