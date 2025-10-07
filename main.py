import time
import threading
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


def repeat_ip_test():
    while True:
        try:
            response = ip_tester()
            print("Periodic Check:", response)
        except Exception as e:
            print("Error during IP test:", e)
        time.sleep(30)

# Start the loop in a separate thread
threading.Thread(target=repeat_ip_test, daemon=True).start()
