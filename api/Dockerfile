FROM python:3.7-slim

COPY ./requirements.txt /requirements.txt
# create root directory for our project in the container
RUN mkdir /api
# COPY ./scripts /scripts
WORKDIR /api

# Copy the current directory contents into the container at /shuddhi
ADD . /api/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt

