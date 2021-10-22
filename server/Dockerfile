FROM nginx:1.18-alpine

COPY nginx.conf /etc/nginx/nginx.conf

CMD uvicorn API_Server:app --host api --port $PORT