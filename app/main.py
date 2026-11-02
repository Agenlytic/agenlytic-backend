
from fastapi import FastAPI

app = FastAPI(
    title="Agenlytic - Api"
)

@app.get('/')
def read_root():
    return {"Hello": "World"}