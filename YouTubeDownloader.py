#USE GOOGLE COLLABORATORY and use cloudconvert or HAVE A SYSTEM THAT PROCESSES WEBM TO AUDIO FILES LIKE MP3 OR FLAC.


# pip install pytube or use packages on the left on side for replit


from pytube import YouTube
from pytube import Playlist


x = input('P or V \nPlaylist or Video?: ')

if x == 'p':
  print('hi')
  # you right click and paste the url in the console
  q = input('')
  p = Playlist(q)

  #playlist 
  print('The title: ', p.title, "\n")
  # print('The Url', p.thumbnail_url, '\n')
  print(f'Downloading: {p.title}')
  x = int(input('itag: '))
  for video in p.videos: video.streams.get_by_itag(x).download()
  #(output_path=f'{p.title}/')

if x == 'v':
  yt = YouTube('https://www.youtube.com/watch?v=ZAiEPUu0iO4')
  print('The title: ', yt.title, "\n")  
  print('The Url', yt.thumbnail_url, '\n')
  stream = yt.streams.get_by_itag(int(input('itag:')))
  input('enter to continue')
  stream.download(output_path='Test musics/')
else:
  print('this is wrong')

