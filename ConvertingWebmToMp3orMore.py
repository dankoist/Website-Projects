from pydub import AudioSegment

#This does not work, I think
aud_file = ['iwan.webm']

for x in aud_file:
  print(x)
#This does work, I assume you can have more than one file to convert into an audio file. The catch is that they

# only convert and overwrite to one file. Apparently 
wav_audio = AudioSegment.from_file('iwan.webm', format="webm")

#idk what this is for
raw_audio = AudioSegment.from_file("iwan.webm", format="raw", frame_rate=44100, channels=2, sample_width=2)           
#The Audio files end up being one name
file_handle = wav_audio.export("iwan.mp3", format="mp3")