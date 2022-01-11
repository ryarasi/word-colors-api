from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from ximilar.client import DominantColorProductClient
import os
import requests


app = FastAPI()

origins = os.getenv('ORIGINS',"*")
port = int(os.getenv('PORT', 8000))
reload = bool(os.getenv('RELOAD', 1))
dev = bool(os.getenv('DEBUG', 0))
host=str(os.getenv('HOST','0.0.0.0'))
GOOGLE_SEARCH_API_KEY=str(os.getenv('GOOGLE_SEARCH_API_KEY',''))
GOOGLE_SEARCH_ENGINE_ID=str(os.getenv('GOOGLE_SEARCH_ENGINE_ID',''))
XIMILAR_API_KEY=str(os.getenv('XIMILAR_API_KEY',''))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_dominant_colors(imgLink):
    generic_client = DominantColorProductClient(token=XIMILAR_API_KEY)
    result = generic_client.dominantcolor([{"_url": imgLink}])
    return result


@app.get('/')
def Home():
    return "Service is Running..."

@app.get('/images')
async def Images(query):
    google_search_api_url = "https://customsearch.googleapis.com/customsearch/v1"+"?q="+query+"&imgColorType=COLOR&imgType=PHOTO&safe=ACTIVE&searchType=image&cx="+GOOGLE_SEARCH_ENGINE_ID+"&key="+GOOGLE_SEARCH_API_KEY

    images_search_response = requests.get(google_search_api_url)
    json_data = images_search_response.json()
    resultsExist = int(json_data['searchInformation']['totalResults']) > 0
    if resultsExist:
        imageObjects = json_data['items']

        imageLinks = []
        for item in imageObjects:
            imageLinks.append(item['link'])

        response = []

        for imageLink in imageLinks:
            dominant_colors = get_dominant_colors(imageLink)
            status = dominant_colors['records'][0]['_status']['code']
            if status == 200:
                colors = dominant_colors['records'][0]['_dominant_colors']['rgb_hex_colors']
                response.append({'image': imageLink, 'colors': colors})

        return response
    else:
        return images_search_response.json()



if __name__ == "__main__":
    uvicorn.run('main:app', port=port, reload=reload, host=host)
