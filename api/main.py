from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

port = os.environ['PORT']
reload = os.environ['RELOAD']

@app.get('/')
def Home():
    return "Service is Running...now"


if __name__ == "__main__":
    uvicorn.run('main:app', port=port, reload=reload, root_path="/")