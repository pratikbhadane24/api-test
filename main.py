from typing import Union
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def ip_tester():
    req = requests.get("https://signals.cirrus.trade/health")
    print("REQUEST", req)
    return {"status": req.status_code, "response": req.json()}
