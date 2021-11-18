from pydub import AudioSegment

wav_audio = AudioSegment.from_file("MountainKing.webm", format="webm")
raw_audio = AudioSegment.from_file("MountainKing.webm", format="raw", frame_rate=44100, channels=2, sample_width=2)           

file_handle = wav_audio.export("output.mp3", format="mp3")