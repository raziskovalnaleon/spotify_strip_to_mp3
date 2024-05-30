import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

CLIENT_ID = 'fd358b97cd2e423e8ddaa71d03bcf9f2'
CLIENT_SECRET = 'e3b7153da9ce4e568cd449cb936ab0e3'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

print(access_token)



