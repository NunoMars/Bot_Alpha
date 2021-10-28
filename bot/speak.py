from gtts import gTTS
#from playsound import playsound
import pyglet

from os import remove, system


def bot_say(text):  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed

    language = 'fr'

    sound = gTTS(text=text, lang=language, slow=False)    
    
    sound.save("voice.mp3")# Saving the converted audio in a mp3 file named

    # playsound("voice.mp3")# Playing the converted file)                                                         


    song = pyglet.media.load('voice.mp3')
    song.play()
    # pyglet.app.run()

    remove("voice.mp3")


