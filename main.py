import aiohttp
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
async def ip_tester():
    url = "https://api.ipify.org?format=json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as resp:
            data = await resp.json()
            return {"egress_ip": data.get("ip"), "status": resp.status}
