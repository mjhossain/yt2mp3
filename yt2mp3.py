from pytube import Search
from pytube import YouTube
import os

# opening the song list file
song_list = open('./song_list.txt', 'r')

# folder path for downloads
download_folder = './downloads'

for song in song_list:
    try:
        # perform YouTube search
        searchHandle = Search(song)

        # create url
        videoUrl = 'https://www.youtube.com/watch?v=' + str(searchHandle.results[0].video_id)
        yt = YouTube(videoUrl)

        # download file as mp3
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=download_folder)
    
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # show results
        print(yt.title + " has been successfully downloaded.")
    except:
        print('Download failed!')
