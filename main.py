import time
import threading
import asyncio
import aiohttp
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
async def ip_tester():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://signals.cirrus.trade/health") as resp:
            status = resp.status
            response = await resp.json()
            return {"status": status, "response": response}


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
