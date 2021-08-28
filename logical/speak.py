from gtts import gTTS
from playsound import playsound
import os

# The text that you want to convert to audio

def bot_say(mytext):  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed

    language = 'fr'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save('file.mp3')

    playsound('file.mp3')
    os.remove('file.mp3')
