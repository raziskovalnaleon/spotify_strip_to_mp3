import os
from pytube import YouTube

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
