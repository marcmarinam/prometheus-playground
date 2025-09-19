from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator()

instrumentator.instrument(app).expose(app)


@app.get("/_health")
async def read_root():
    return "OK"
