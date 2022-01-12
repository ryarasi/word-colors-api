# Word to Colors Generator API

This app takes in a word (or a phrase) as input and shows you associated colors of the object that the word or phrase represents.

Link to app deployed on cloud - https://ragav-word-colors.netlify.app/

Link to the API deployed on the cloud - https://word-colors-api.herokuapp.com

Link to UI code - https://github.com/ryarasi/word-colors

# Basic info

- This project is a dockerized FastAPI-based API with one endpoint that serves the word-colors app linked above.
- All API secret keys for Google Search API and Ximilar API are stored safely as env variables.

# Notable Packages/Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - A very lightweight, performant and efficient python-based API
- [Google Custom Search API](https://developers.google.com/custom-search/v1) - This is the primary API that we use to get images associated with search queries
- [ximilar-client](https://pypi.org/project/ximilar-client/) - A wrapper for the [Ximilar API](https://www.ximilar.com/all-services/) services which offer AI-based visual API services.

# Methodology

- When the API receives the GET request from the client with the search term, we make a request to the Google Custom Search Engine API to request images for that query.
- We get an array of upto 10 image urls as a response
- We run these image urls through Ximilar API to get an array of dominant colors for each of those images.
- The API has means to access the Google Custom Search API, which it uses to search for images for the query.
- When the images return, we use the [Ximilar API](https://www.ximilar.com/all-services/) package to get an array of dominant colors as hex codes.
- The API then neatly organizes the image links and the dominant colors for each image into a JSON and sends it back to the client.

# How to run this app on your local machine

- Download this code to your local machine
- Make sure you have Python 3 installed. [Instructions](https://www.python.org/downloads/)
- Make sure you have Docker and Docker Compose installed. [Instructions](https://docs.docker.com/compose/install/)
- Duplicate the `env.sample` file and rename it as `.env` and populate it with the API keys. You can obtain them by visiting the links shown there.
- Make sure to populate it with the necessary API keys
- Open your terminal and change directory to the project root folder and enter `npm start` to get started.
- The API will be served and it can be accessed at `http://0.0.0.0:/8000`
