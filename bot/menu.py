from speak import bot_say
from listen import reccord_audio


bot_say("Bonjour, que puis-je faire pour vous?")
bot_reccord = reccord_audio()

if bot_reccord["success"] == "True":
    bot_say("Vous avez dit: " + bot_reccord['transcription'])
    bot_say("je vérifie, patientez...")
else :
    bot_say("Je n'ai pas compris")
    bot_say("Pour connaitre la liste de ce que je sais déja, faire dites Menu")
    bot_reccord = reccord_audio()
    
