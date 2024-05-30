import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

CLIENT_ID = 'client_id'
CLIENT_SECRET = 'client_secret'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# This creates access token that expires after aproximetly 1 hour
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



