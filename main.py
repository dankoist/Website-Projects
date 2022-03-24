from pytube import Channel
from pytube import Playlist
from pytube import YouTube
from pydub import AudioSegment
import os

ls = []
c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
# for videos in c.videos:
#   print(videos)
for url in c.video_urls[:3]:
  print(url)



p = Playlist('https://youtube.com/playlist?list=OLAK5uy_kogOCcCSJj35BNnHBOHHq4ueqasxkFP8g')
tit = f'{p.title}'
for videos in p.videos:
  ls.append(videos)
  


how_many_vids = len(ls)
# x = int(input("how many songs? \n"))
arts = input("What is the artist's name? \n")
for url in p.video_urls[:how_many_vids]:
  print('\n', url)
  yt = YouTube(f'{url}')
  y = yt.title
  print(y, yt.thumbnail_url, '\n')
  yt.streams.get_by_itag(251).download(output_path = tit)
  os.chdir(tit)
  # more = os.getcwd()
  # stuf = f"{more}/{tit}/{y}/"
  Aud_webm = AudioSegment.from_file(f"{y}.webm", format = 'webm')
  Aud_webm.export(f"{y}", format="mp3", bitrate = '192k', tags={'artist': f'{arts}', 'album': f'{tit}', 'comments': 'Test'})

# from pytube import Channel
# from pytube import Playlist
# from pytube import YouTube

# c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
# for url in c.video_url[:]:
#   print(url)



# p = Playlist('https://youtube.com/playlist?list=OLAK5uy_lgHUFYtG3rJleXQLOxCbq4QQo0wIk5C1o')
# for videos in p.videos:
#   print(videos)
#   print(videos.url)


# yt = YouTube('https://www.youtube.com/watch?v=acvIVA9-FMQ')
# print(yt.title, yt.thumbnail_url)


# from pytube import Playlist
# from pydub import AudioSegment

# p = Playlist('')

# base_dir = f"{p.title}"

# print(f"\nINFO:\nTitle:{p.title}\n")

# for videos in p.videos:
#   videos.streams.get_by_itag(251).download(output_path=f'{p.title}')






# webm_audio = AudioSegment.from_file(f'a.webm', format="webm")



# #idk what this is for
# raw_audio = AudioSegment.from_file(f'a.webm', format="raw", frame_rate=44100, channels=2, sample_width=2)           
# #The Audio files end up being one name
# file_handle = webm_audio.export(f"{ERROR}.mp3", format="mp3",bitrate = "192k", tags={"album": f"{p.title}", "artist": f"{x}"})