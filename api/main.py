from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
host = str(os.getenv('HOST','0.0.0.0'))


@app.get('/')
def Home():
    return "Service is Running..."


if __name__ == "__main__":
    uvicorn.run('main:app', port=port, reload=reload, host=host, root_path="/")
