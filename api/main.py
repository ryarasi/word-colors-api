from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def Home():
    return "Service is Running...now"


if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, reload=False, root_path="/")