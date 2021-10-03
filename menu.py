from bot.speak import bot_say
from bot.listen import reccord_audio
from bot.constants import *


def bot_menu():
    """app menu"""
    bot_say("Bonjour... session initialisée...")

    while True:
        bot_reccord = reccord_audio()
        if bot_reccord in MENU_ITEMS:
            bot_say(MENU_ITEMS_DICT[bot_reccord])
            break
        elif START_SESSION in bot_reccord:
            bot_say("Bonjour, je suis ALPHA, l'assistant de la maison de l'écologie, je peux vous aider à répondre à vos questions")
            break
        elif bot_reccord in CLOSE_SESSION:
            bot_say("Au revoir, je vous reviens bientôt")
            break
        else:
            bot_say(MENU_ITEMS_DICT["error"])
            break
            

"""if START_SESSION in choice: #commencer la commande par Alpha
for item in choice:
    if item in menu_items:
        if choice[choice.index(item) + 2:] == IndexError:
            bot_say(menu_items_dict[item])
        else:
            new_choice = " ".join(choice[choice.index(item) + 2:])
            print(new_choice)
            # print(menu_items_dict[item(new_choice)])
            # bot_say(menu_items_dict[item](new_choice))
    else:
        bot_say(menu_items_dict["error"])

elif choice == CLOSE_SESSION:
bot_say("Au revoir, session terminé!")
break
else:
bot_say(menu_items_dict["error"])
continue"""

