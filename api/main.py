from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = os.getenv('ORIGINS',"*")
port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
host=str(os.getenv('HOST','0.0.0.0'))


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
