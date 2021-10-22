FROM python:3.7-slim

WORKDIR /api

COPY . .

RUN pip install -r requirements.txt

CMD uvicorn API_Server:app --host api --port $PORT
