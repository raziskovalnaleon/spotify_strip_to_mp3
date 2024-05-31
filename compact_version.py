import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
from spotifysearch.client import Client
from youtubesearchpython import Search
import os
from pytube import YouTube


CLIENT_ID = 'fd358b97cd2e423e8ddaa71d03bcf9f2'
CLIENT_SECRET = 'e3b7153da9ce4e568cd449cb936ab0e3'

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

print(f"Access token: {access_token}")
print('-'*80)

CLIENT_ID = 'fd358b97cd2e423e8ddaa71d03bcf9f2'
CLIENT_SECRET = 'e3b7153da9ce4e568cd449cb936ab0e3'
AUTH_URL = 'https://accounts.spotify.com/api/token'

PLAYLIST_LINK = "https://open.spotify.com/playlist/2myW2EQLU9T5h6s6hKvOid?si=e72ff2584e6045cb"
PLAYLIST_URI = PLAYLIST_LINK.split("/")[-1].split("?")[0]

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
myclient = Client(CLIENT_ID, CLIENT_SECRET)

final_track_list = list()

len_for_precent = len(sp.playlist_tracks(PLAYLIST_URI)["items"])
print(f"{len_for_precent} songs on this album")
# Fetching all the songs names, youtube links 

for x,track in enumerate(sp.playlist_tracks(PLAYLIST_URI)["items"]):
    track_name = track["track"]["name"]
    track_uri = track["track"]["uri"]
    artist_name = track["track"]["artists"][0]["name"]

    search_word = f"{track_name}{artist_name}"
    allSearch = Search(search_word, limit = 1)
    # print(track)
    # print(f"{track_uri}---{track_name}---{artist_uri}---{artist_name}")
    final_track_list.append(f"{track_name},{artist_name},{track_uri},{allSearch.result()['result'][0]['link']}")
    precent_for_show = ((x + 1) / len_for_precent) * 100
    print(f"{int(precent_for_show)}% completed")
# Writing data int .txt file
with open('links.txt', 'a') as f:
    for idi, item in enumerate(final_track_list):
        print(f"{idi + 1}-{item.split(',')}")
        if(len_for_precent == idi + 1):
            f.write(item)
        else:
            f.write(item + "\n")


print('*'*80)
print("DOWNLOAD STARTED")
print('*'*80)

file_links = open('links.txt', 'r')

final_track_list = file_links.read().split('\n')
# print(final_track_list)

downloadable_url_list = list()
# Downloading songs
for item in final_track_list:
    # print(item.split(','))
    try:
        downloadable_url_list.append(item.split(',')[3])
    except:
        print('No downloadable links on .txt file')
        break
if(len(downloadable_url_list) != 0):
    for idlink, link in enumerate(downloadable_url_list):
        try:
            print(f"{idlink + 1}:{link}")
            # test_link = link
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()
            destination = './songs/'
            out_file = video.download(output_path=destination)  # file saves as 'mp4'
            base, ext = os.path.splitext(out_file)  # 'cuts' the mp4 part
            new_file = base + '.mp3'  # creates a file with mp3 end
            os.rename(out_file, new_file)  # and it renames it
            print(yt.title + " has been successfully downloaded.")
        except:
            print("Can not download this link")
else:
    print("Nothing to download")

file_links.close()

