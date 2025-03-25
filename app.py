import fastapi
import uvicorn

app = fastapi.FastAPI()

items = ["one", "two", "three"]

@app.get("/")
def index():
    return {"message": "Hello, World"}  

@app.get("/items")
def read_items():
    return items