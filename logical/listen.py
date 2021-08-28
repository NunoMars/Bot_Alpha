from speech_recognition import Recognizer, Microphone
from speak import bot_say

recognizer = Recognizer()
# On enregistre le son
with Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    bot_say("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler...")
    bot_say("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    print("Enregistrement terminé !")
    bot_say("Enregistrement terminé !")
    
# Reconnaissance de l'audio
try:
    print("Reconnaissance du texte...")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
    print("Vous avez dit : {}".format(text))
    bot_say("Vous avez dit : {}".format(text))
except Exception as ex:
    print(ex)