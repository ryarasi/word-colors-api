from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from ximilar.client import DominantColorProductClient
import os
import requests


app = FastAPI()


# Getting the necessary variables from the environment variables

origins = os.getenv('ORIGINS',"*")
port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
dev = bool(os.getenv('DEBUG', 0))
host=str(os.getenv('HOST','0.0.0.0'))
GOOGLE_SEARCH_API_KEY=str(os.getenv('GOOGLE_SEARCH_API_KEY',''))
GOOGLE_SEARCH_ENGINE_ID=str(os.getenv('GOOGLE_SEARCH_ENGINE_ID',''))
XIMILAR_API_KEY=str(os.getenv('XIMILAR_API_KEY',''))

# Setting the accepted origins here for CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#  Method to obtain dominant colors from an image URL
def get_dominant_colors(imgLink):
    generic_client = DominantColorProductClient(token=XIMILAR_API_KEY)
    result = generic_client.dominantcolor([{"_url": imgLink}])
    return result

# Placeholder root path
@app.get('/')
def Home():
    return "Service is Running..."

# The main url used by the client for the word to colors feature.
# Takes in a "query" as URL params to do everything
@app.get('/images')
async def Images(query):
    #  We first construct the URL using the variables sourced from the environemnt variables
    google_search_api_url = "https://customsearch.googleapis.com/customsearch/v1"+"?q="+query+"&imgColorType=COLOR&imgType=PHOTO&safe=ACTIVE&searchType=image&cx="+GOOGLE_SEARCH_ENGINE_ID+"&key="+GOOGLE_SEARCH_API_KEY

    # We make a GET request and store the response
    images_search_response = requests.get(google_search_api_url)

    # Convert the response into JSON format
    json_data = images_search_response.json()

    # Check if the results actually exist. Sometimes no results are shown because safe search is active and the query may be NSFW
    resultsExist = int(json_data['searchInformation']['totalResults']) > 0
    if resultsExist:

        # If results exist, then we collect the image objects as an array
        imageObjects = json_data['items']


        # Extract only the URLs of the images into a variable
        imageLinks = []
        for item in imageObjects:
            imageLinks.append(item['link'])

        response = []
        
        # Loop through each of those image URLs
        for imageLink in imageLinks:
            # Get its dominant colors
            dominant_colors = get_dominant_colors(imageLink)
            # Get the status code of that request to the Ximilar API
            status = dominant_colors['records'][0]['_status']['code']
            if status == 200:
                # If that request was successful, we proceed to append to the final response, our image URL and its dominant colors
                colors = dominant_colors['records'][0]['_dominant_colors']['rgb_hex_colors']
                response.append({'image': imageLink, 'colors': colors})

        # Finally return the response
        return response
    else:
        # In case we don't get any results we send the original image search response
        return images_search_response.json()



if __name__ == "__main__":
    uvicorn.run('main:app', port=port, reload=reload, host=host)
