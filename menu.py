from bot.speak import bot_say
from bot.listen import reccord_audio
from bot.constants import CLOSE_SESSION, MENU_ITEMS_DICT, START_SESSION


def bot_menu():
    """app menu"""
    bot_say("Bonjour... j'écoute...")

    while True:
        bot_reccord = reccord_audio()

        if bot_reccord == START_SESSION:
            bot_say("Oui, je suis prête!!")

            while True:
                bot_reccord = reccord_audio()
                print(bot_reccord)
                if bot_reccord is None:
                    continue               
            
                elif bot_reccord == CLOSE_SESSION:
                    bot_say("au revoir")
                    break    
                args= bot_reccord[1]
                print(args)
                bot_say(MENU_ITEMS_DICT[bot_reccord[0]](args))
"""if START_SESSION in choice: #commencer la commande par Alpha
for item in choice:
    if item in menu_items:
        if choice[choice.index(item) + 2:] == IndexError:
            bot_say(menu_items_dict[item])
        else:
            new_choice = " ".join(choice[choice.index(item) + 2:])
            print(new_choice)
            # print(menu_items_dict[item(new_choice)])
            # bot_say(menu_items_dict[item](new_choice))"""


