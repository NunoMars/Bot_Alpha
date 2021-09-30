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
    
    # Saving the converted audio in a mp3 file named


    sound.save("voice.mp3")

    try:
        directory = path.dirname(path.dirname(__file__))# we get the right path.
        path_to_file = path.join(directory, "voice.mp3")

        playsound(path_to_file)                                                         

        remove("voice.mp3")
    except:
        print("error")
        remove("voice.mp3")

