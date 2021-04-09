import subprocess
import youtube_dl
from bs4 import BeautifulSoup as bs
import requests
from youtubesearchpython import *
import os




def download_playlist_tracks(url, target_folder):
    playlist = Playlist(url)
    while playlist.hasMoreVideos:
        playlist.getNextVideos()

    album_title = playlist.info['title']
    album_title = album_title.replace(' ', '_')
    if not os.path.exists('{target_folder}/{album_title}'):
        os.makedirs('{target_folder}/{album_title}')

    for i in range(len(playlist.videos)):
        url = playlist.videos[i]['link']
        bashCommand = f'youtube-dl -x -f bestaudio[ext=m4a] --add-metadata --embed-thumbnail -o {target_folder}/{album_title}/{playlist.videos[i]["title"].replace(" ", "_")}.%(ext)s {url}'
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(f"{i+1}/{len(playlist.videos)}")

url = input("Paste a link to youtube playlist: ")
target_folder = input("Enter directory where to download. For example '/home/user/Music)': ")
download_playlist_tracks(url, target_folder)
