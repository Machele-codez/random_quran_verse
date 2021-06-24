import requests
import tempfile
import subprocess
import random
import time 

surah_list=list(range(2,4))

surah_verses = {
	1: (1, 7),
	2: (253, 286),
	3: (1, 32),
	4: (1, 65),
}

# functin to generate random verses within a specified range
#def generate_verse(surah1, verse1, surah2, verse2):
def generate_verse():
  #surah = random.choice(range(surah1, surah2 + 1))
  surah = random.choice(surah_list)

  selected_surah_verse_range = surah_verses[surah]

  verse = random.choice(range(*selected_surah_verse_range))

  verse_key = f"{surah}:{verse}"
  print(verse_key)

  response = requests.get(f"https://api.quran.com/api/v4/verses/by_key/{verse_key}?language=en&words=false&audio=11")
  response = response.json()

  audio_url = response["verse"]["audio"]["url"]
  audio_url = "https:" + audio_url
  print(audio_url)

  audio = requests.get(audio_url)
  audio_file = tempfile.NamedTemporaryFile(delete=False)
  open(audio_file.name, "wb").write(audio.content)
  print(audio_file.name)

  return audio_file.name


# countdown function to allow user to recite before next verse generation
def countdown (time_secs):
  """
  function to create a countdowm timer to be displayed
  :param: time_secs is the duration of the countdown
  """

  while time_secs >= 0:
    mins, secs = divmod(time_secs, 60)
    print("{:02d}:{:02d}".format (mins, secs), end="\r")
    time.sleep(1)
    time_secs -=1


# main program
counter = 1
"""
start_surah = input("Enter surah number to begin from: ")
start_surah_verse = input("Enter verse number to begin from: ")
end_surah = input("Enter surah number to end at: ")
end_surah_verse = input("Enter surah number to end at: ")
"""
for _ in range(30):
  print("count", counter)
  """
  verse_audio_file = generate_verse(
	start_surah, start_surah_verse,
	end_surah, end_surah_verse
	)
  """
  verse_audio_file = generate_verse()

  hasbuk_file = "hasbuk.m4a"
  iqra_file = "iqra.m4a"

  subprocess.call('play-audio '+ iqra_file, shell=True)
  subprocess.call('play-audio '+ verse_audio_file, shell=True)

  countdown (120) # wait
  subprocess.call('play-audio '+ hasbuk_file, shell=True)

  time.sleep(10)
  subprocess.call('rm '+ verse_audio_file, shell=True)
  counter += 1
