from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
host=str(os.getenv('HOST','0.0.0.0'))

@app.get('/')
def Home():
    return "Service is Running..."

@app.get('/images')
def Images(query):
    return "Here are the images for the query " + query


if __name__ == "__main__":
    print('port => ', port)
    print('reload => ', reload)
    print('host => ', host)
    uvicorn.run('main:app', port=port, reload=reload, host=host)
