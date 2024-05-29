import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
import pandas as pd
from spotifysearch.client import Client
from youtubesearchpython import Search



CLIENT_ID = 'fd358b97cd2e423e8ddaa71d03bcf9f2'
CLIENT_SECRET = 'e3b7153da9ce4e568cd449cb936ab0e3'
# Here at PLAYLIST_LINK you can put whatever spotify link of album you want. WARNING: it will strip 100 songs per round
# PLAYLIST_LINK = "https://open.spotify.com/playlist/3vP9BQxraLqDolt4wuiB0C?si=d5d53b7325944827" # rock 1 --> 100 songs 
PLAYLIST_LINK = "https://open.spotify.com/playlist/2myW2EQLU9T5h6s6hKvOid?si=e72ff2584e6045cb" # rock 2 --> 47 songs
PLAYLIST_URI = PLAYLIST_LINK.split("/")[-1].split("?")[0]

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
myclient = Client(CLIENT_ID, CLIENT_SECRET)


final_track_list = list()

len_for_precent = len(sp.playlist_tracks(PLAYLIST_URI)["items"])
# Fetching all the songs names, youtube links 
for x,track in enumerate(sp.playlist_tracks(PLAYLIST_URI)["items"]):
    track_name = track["track"]["name"]
    track = myclient.search(track_name).get_tracks()[0]
    search_word = f"{track.artists[0].name}{track.name}"
    allSearch = Search(search_word, limit = 1)
    # print(track)
    # print(f"{track_uri}---{track_name}---{artist_uri}---{artist_name}")
    final_track_list.append(f"{track.name},{track.artists[0].name},{track.url},{allSearch.result()['result'][0]['link']}")
    precent_for_show = ((x + 1) / len_for_precent) * 100
    print(f"{int(precent_for_show)}% completed")
# Writing data int .txt file
with open('links.txt', 'a') as f:
    for idi, item in enumerate(final_track_list):
        print(f"{idi + 1}-{item.split(',')}")
        f.write(item + "\n")