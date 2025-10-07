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
