from gtts import gTTS
from playsound import playsound

import os


def bot_say(mytext):  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed

    language = 'fr'

    sound = gTTS(text=mytext, lang=language, slow=False)
    
    # Saving the converted audio in a mp3 file named

    """ import sys
    if "D:\\my_sound_folder" not in sys.path:
        sys.path.append("D:\\my_sound_folder")"""
    sound.save("voice.mp3")

    try:
        s_musicfile = "/Users/Loupy/Onedrive/Bureau/chifoumi_speak_test/voice.mp3"

        #s_musicfile = s_musicfile.replace(" ", "%20")

        playsound(s_musicfile)                                                         

        os.remove("voice.mp3")
    except:
        print("error")
        os.remove("voice.mp3")

