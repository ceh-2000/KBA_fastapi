import requests
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

url = "http://128.232.144.89:8000/v0/scope"

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

@app.get("/")
async def root(auth: str, wkt: str):
    headers = {"Authorization": "Bearer " + auth, "WKT": wkt}

    r = requests.get(url=url, headers=headers)

    return r.json()
