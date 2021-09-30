from bot.speak import bot_say
from bot.listen import reccord_audio
from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki


def bot_menu():
    """app menu"""

    menu_items =["alpha", "météo", "jouer", "heure", "date", "wikipedia"]
    CLOSE_SESSION = "au revoir alpha"
    while True:
        bot_reccord = reccord_audio()
        choice = bot_reccord["transcription"].split()

        if choice[0] in menu_items:
            if choice[choice.index("météo") + 2:] != []:
                city = choice[choice.index("météo") + 2:].join(" ")
                bot_say(weather_forecast(city))

            else:
                bot_say("vous voulez la météo sur quelle ville?")
                #récupérer la ville   
                while True:
                    bot_reccord = reccord_audio()
                    if bot_reccord["success"] == True:
                        city = bot_reccord["transcription"]
                        bot_say(weather_forecast(city.lower()))
                        break
                    else:
                        bot_say("Pouvez-vous répéter la ville s'il vous plait ?")

        elif choice[0] in menu_items and choice[choice.index("jouer") + 2:] != []:
            bot_say("Je pourrait bientôt le faire .. je j'aprends tous les jours !")

        elif choice[0] in menu_items and choice[choice.index("heure") + 2:] != []:
            bot_say(get_time_now()[1])

        elif choice[0] in menu_items and choice[choice.index("date") + 2:] != []:
            bot_say(get_time_now()[0])

        elif choice[0] in menu_items and choice[choice.index("propos") + 2:] != []:
            item = choice[choice.index("propos") + 2:]
            if len(item) == 1:
                bot_say(" Selon wikipedia " + call_wiki(item))
            else:
                items = choice[choice.index("propos") + 2:].join(" ")
                bot_say(" Selon wikipedia " + call_wiki(items))
        else:
            bot_say(bot_reccord["error"])
            break
            
""" if WAKE in bot_reccord["transcription"].lower():#open session

    bot_say("Oui, je suis prête, que voulez-vous?")
    bot_reccord = reccord_audio()

    choice = bot_reccord["transcription"].split()
    print(choice)

    test_in_list = bot_reccord["transcription"].split()
    print(test_in_list)

    if bot_reccord["success"] == True:

        if 'menu' in test_in_list:
            bot_say("Ok, voilà ce que je sais déjà faire ..." + str([i for i in menu_items]) + ".")


        if "météo" in test_in_list:
            if test_in_list[test_in_list.index("météo") + 2:] != []:
                city = test_in_list[test_in_list.index("météo") + 2:].join(" ")
                bot_say(weather_forecast(city))
                continue
            else:
                bot_say("vous voulez la météo sur quelle ville?")
                #récupérer la ville   
                while True:
                    bot_reccord = reccord_audio()
                    if bot_reccord["success"] == True:
                        city = bot_reccord["transcription"]
                        bot_say(weather_forecast(city.lower()))
                        break
                    else:
                        bot_say("Pouvez-vous répéter la ville s'il vous plait ?")
                        continue 


        if "l'heure" in test_in_list or "heure" in test_in_list:
            bot_say(get_time_now()[1])
            continue

        if "date" in test_in_list or "jour" in test_in_list:
            bot_say(get_time_now()[0])
            continue                

        if "propos" in test_in_list:
            item = test_in_list[test_in_list.index("propos") + 2:]
            if len(item) == 1:
                bot_say(" Selon wikipedia " + call_wiki(item))
            else:
                items = test_in_list[test_in_list.index("propos") + 2:].join(" ")
                bot_say(" Selon wikipedia " + call_wiki(items))
            continue
        else:
            bot_say(bot_reccord["error"])

    
    else :
        bot_say(bot_reccord["transcription"])
        bot_say("Pour connaître la liste de ce que je sais déjà faire... dites Menu")
        

if CLOSE_SESSION in bot_reccord["transcription"].lower():
    bot_say("ok je ferme la session!")
    break"""