import pyttsx3
eCompanion = pyttsx3.init()
speech = input ("Type what you want to hear: ")
eCompanion.say(speech)
eCompanion.runAndAwait()  
