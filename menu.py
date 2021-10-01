from bot.speak import bot_say
from bot.listen import reccord_audio
from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki


def bot_menu():
    """app menu"""

    menu_items =["météo", "jouer", "heure", "date", "wikipedia"]
    menu_items_dict = {
        "date" : get_time_now()[0],
        "heure" : get_time_now()[1],
        "météo" : weather_forecast(),
        "jouer" :"Je pourrait bientôt le faire .. je j'aprends tous les jours !",
        "wikipedia" : call_wiki(),
        "error" : "Je n'ai pas compris votre demande, veuillez réessayer",
    }
    START_SESSION = "alpha"
    CLOSE_SESSION = "au revoir alpha"
    
    while True:
        bot_reccord = reccord_audio()
        choice = bot_reccord["transcription"].split()
        print(choice)
        if choice[0] == START_SESSION and choice != []: #commencer la commande par Alpha et tester si la liste est vide

            for item in choice:
                if item in menu_items:
                    if choice[choice.index(item) + 2:].join(" ") == "":
                        bot_say(menu_items_dict[item])
                    else:
                        new_choice = choice[choice.index(item) + 2:].join(" ")
                        bot_say(menu_items_dict[new_choice])
                else:
                    bot_say(menu_items_dict["error"])
                    
        elif choice == CLOSE_SESSION:
            bot_say("Au revoir, session terminé!")
            break
        else:
            bot_say(menu_items_dict["error"])
            continue


    """ if "météo" in choice:
        try:
            city = choice[choice.index("météo") + 2:].join(" ")
            bot_say(weather_forecast(city))

        except IndexError:
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

    elif "jouer" in choice:
        menu_items_dict["jouer"]

    elif "heure" in choice:
        menu_items_dict["heure"]

    elif "date" in choice:
        menu_items_dict["date"]

    elif "propos" in choice:
        item = choice[choice.index("propos") + 2:]
        if len(item) == 1:
            bot_say(" Selon wikipedia " + call_wiki(item))
        else:
            items = choice[choice.index("propos") + 2:].join(" ")
            bot_say(" Selon wikipedia " + call_wiki(items))
else:
    menu_items_dict["error"]
    break"""
            
