from gtts import gTTS
from playsound import playsound

from os import remove, path


def bot_say(mytext):  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed

    language = 'fr'

    sound = gTTS(text=mytext, lang=language, slow=False)
    
    
    directory = path.dirname(path.dirname(__file__))# we get the right path.

    sound.save("voice.mp3")# Saving the converted audio in a mp3 file named
       
    file_name = path.join(directory, "voice.mp3")

    playsound("voice.mp3")# Playing the converted file)                                                         

    remove("voice.mp3")


