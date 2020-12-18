from gtts import gTTS 
import time
from mutagen.mp3 import MP3
import os
  
# usage: git bash: python P:/Mini-Python/speech-recognition/text-to-speech.py

print("Input: ", end="")
# inputs the text that you want to convert to audio 
mytext = input()

# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# sets up the file name
file_name = "welcome.mp3"
# Saving the converted audio in a mp3 file
myobj.save(file_name)

os.system(file_name) 


