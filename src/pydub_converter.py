import pydub
from pydub import AudioSegment

guitar_m4a = AudioSegment.from_file("./music/Basic Guitar.m4a", format="m4a")

guitar_m4a.export("./music/Basic Guitar.mp3", format="mp3")