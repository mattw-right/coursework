

from pydub import AudioSegment

sound = AudioSegment.from_mp3("t.mp3")
sound.export("file.wav", format="wav")
