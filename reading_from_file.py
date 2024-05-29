import os
from pytube import YouTube

file_links = open('links.txt', 'r')

final_track_list = file_links.read().split('\n')

downloadable_url_list = list()
# Downloading songs
for item in final_track_list:
    # print(item.split(','))
    downloadable_url_list.append(item.split(',')[3])
for idlink, link in enumerate(downloadable_url_list):
    print(f"{idlink + 1}:{link}")
    # test_link = link
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    destination = './songs/' # set destination whereever you want
    out_file = video.download(output_path=destination)  # file saves as 'mp4'
    base, ext = os.path.splitext(out_file)  # 'cuts' the mp4 part
    new_file = base + '.mp3'  # creates a file with mp3 end
    os.rename(out_file, new_file)  # and it renames it
    print(yt.title + " has been successfully downloaded.")


file_links.close()
