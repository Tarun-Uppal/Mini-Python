# Program to measure the similarity between  
# two sentences using cosine similarity.
from urllib.request import CacheFTPHandler
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import speech_recognition as sr 
import time

# if you cant install pyaudio install pipwin and then using pipwin install pyaudio
# pip install pipwin
# pipwin install pyaudio
# pip install speechRecognition
def main():
    # only do it when you run the program for the first time
    # nltk.download("all")
    
    # X = "The population of asia is 10 million.".lower()
    X = input("Real Answer: ").lower().strip()
    X = X.split('.')
    final_answer = True

    temp = input("1 to type the answer \n2 to dictate the answer \nnothing to exit: ")
    if temp == "e":
        exit()

    Y = ""
    if temp == "1":
        Y = input("Answer: ")    
    if temp == "2":
        Y = getSaidWords()
        # if "." not in Y:
        #     Y += ". "
    Y = Y.lower().strip()
    Y = Y.split(".")
    # difference_between_2_sentences(X, Y)

    for line1 in X:
        temp = False
        for line2 in Y:
            try:
                temp1 = difference_between_2_sentences(line1, line2)
            except ZeroDivisionError:
                print("", end="")
            if temp1 == True:
                temp = True
        if temp == False:
            final_answer = False
        else:
            final_answer = True
    
    if final_answer == True:
        print("GO TO NEXT PART or NEXT CHAPTER")
    else:
        print("GO AND STUDY")
    
def difference_between_2_sentences(X, Y):
    # tokenization 
    X_list = word_tokenize(X)  
    Y_list = word_tokenize(Y) 
    
    # sw contains the list of stopwords 
    sw = stopwords.words('english')  
    l1 =[];l2 =[] 
    
    # remove stop words from the string 
    X_set = {w for w in X_list if not w in sw}  
    Y_set = {w for w in Y_list if not w in sw} 
    
    # form a set containing keywords of both strings  
    rvector = X_set.union(Y_set)  
    for w in rvector: 
        if w in X_set: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0) 
    c = 0
    
    # cosine formula  
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    print("similarity: ", cosine) 
    if cosine >= 1:
        # print("correct")
        return True
    else:
        # print("wrong")
        return False

def getSaidWords():
   #Sample rate is how often values are recorded 
   sample_rate = 48000
   #Chunk is like a buffer. It stores 2048 samples (bytes of data)
   chunk_size = 2048
   #Initialize the recognizer 
   r = sr.Recognizer()
   
   with sr.Microphone(device_index = 0, sample_rate = sample_rate,  
                           chunk_size = chunk_size) as source: 
      #adjust the energy threshold based on the surrounding noise level 
      r.adjust_for_ambient_noise(source) 
      print("Say Something")
      time.sleep(0.1)
      #listens for the user's input 
      audio = r.listen(source) 
            
      try: 
         text = r.recognize_google(audio) 
         print("you said: " + text)  
         return text

      #error occurs when google could not understand what was said 
      except sr.UnknownValueError: 
         print("Google Speech Recognition could not understand audio") 
      except sr.RequestError as e: 
         print("Could not request results from Google Speech Recognition service; {0}".format(e))
main()