
from fastapi import FastAPI

app = FastAPI(
    title="Agenlytic - Api",
    version="1.0.0",
)


@app.get('/')
def read_root():
    return {"Hello": "World"}