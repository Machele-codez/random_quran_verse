import requests
import tempfile
import subprocess
import random

surah_list=[2,3]
surah = random.choice(surah_list)

surah_verses = {
	1: 7,
	2: 286,
	3: 200,
}
no_of_verses = surah_verses[surah]
selected_surah_verse_list = list(range(1, no_of_verses+1))
verse = random.choice(selected_surah_verse_list)

verse_key = f"{surah}:{verse}"
print(verse_key)

response = requests.get(f"https://api.quran.com/api/v4/verses/by_key/{verse_key}?language=en&words=false&audio=6")
response = response.json()

audio_url = response["verse"]["audio"]["url"]
audio_url = "https:" + audio_url
print(audio_url)

audio = requests.get(audio_url)
audio_file = tempfile.NamedTemporaryFile()
open(audio_file.name, "wb").write(audio.content)
print(audio_file.name)

#exit()

subprocess.call('play-audio '+ audio_file.name, shell=True)
subprocess.call('rm '+ audio_file.name, shell=True)
