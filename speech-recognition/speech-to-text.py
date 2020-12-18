#Python 2.x program for Speech Recognition 
  
import speech_recognition as sr 
import time

# usage: git bash: python P:/Mini-Python/speech-recognition/speech-to-text.py

def getSaidWords():
   #Sample rate is how often values are recorded 
   sample_rate = 48000
   #Chunk is like a buffer. It stores 2048 samples (bytes of data)
   chunk_size = 2048
   #Initialize the recognizer 
   r = sr.Recognizer()
   
   #use the microphone as source for input. Here, we also specify  
   #which device to specifically look for incase the microphone  
   #is not working, an error will pop up saying "device_id undefined" 
   with sr.Microphone(device_index = 0, sample_rate = sample_rate,  
                           chunk_size = chunk_size) as source: 
      #wait for a second to let the recognizer adjust the  
      #energy threshold based on the surrounding noise level 
      r.adjust_for_ambient_noise(source) 
      print("Say Something")
      time.sleep(0.1)
      #listens for the user's input 
      audio = r.listen(source) 
            
      try: 
         text = r.recognize_google(audio) 
         print("you said: " + text)  
      
      #error occurs when google could not understand what was said 
         
      except sr.UnknownValueError: 
         print("Google Speech Recognition could not understand audio") 
         
      except sr.RequestError as e: 
         print("Could not request results from Google Speech Recognition service; {0}".format(e))

getSaidWords()
