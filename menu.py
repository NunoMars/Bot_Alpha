from bot.speak import bot_say
from bot.listen import reccord_audio
from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki


def bot_menu():
    menu_items =["météo", "jouer", "heure", "date", "wikipedia"]
    WAKE = "bonjour alpha"
    CLOSE_SESSION = "au revoir alpha"
    while True:
        bot_reccord = reccord_audio()

        if WAKE in bot_reccord["transcription"].lower():
            bot_say("Oui, je suis pête, que voulez-vous?")
            bot_reccord = reccord_audio()
        
            choice = bot_reccord["transcription"].lower()
            print(choice)

            test_in_list = bot_reccord["transcription"].split()
            print(test_in_list)

            if bot_reccord["success"] == True:

                if 'menu' in test_in_list:
                    bot_say("Ok, voilà ce que je sais déja faire ..." + str([i for i in menu_items]) + ".")


                if "météo" in test_in_list:
                    weather_forecast()


                if "l'heure" in test_in_list:
                    bot_say(get_time_now()[1])


                if "date" in test_in_list or "jour" in test_in_list:
                    bot_say(get_time_now()[0])                

                if "a propos" in test_in_list or "me dire sur" in test_in_list:
                    bot_say(call_wiki(bot_reccord["transcription"]))

                else:
                    bot_say("Je ne comprends pas, veuillez répéter.")

            
            else :
                bot_say(bot_reccord["transcription"])
                bot_say("Pour connaitre la liste de ce que je sais déja faire... dites Menu")
                continue

        if CLOSE_SESSION in bot_reccord["transcription"].lower():
            bot_say("ok je ferme la session!")
            break