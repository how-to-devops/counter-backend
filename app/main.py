import logging
import uvicorn
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/count")
async def count():
    return "ok"

if __name__ == "__main__":
    uvicorn.run(app=app, log_config=None, host="0.0.0.0", port=8000)
