from gtts import gTTS
from playsound import playsound
import os


def bot_say(mytext):  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed

    language = 'fr'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named
    # file
    
    myobj.save("voice.mp3")

    try:
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except:
        os.remove("voice.mp3")