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

                if bot_reccord is None:
                    continue               
                    
                elif bot_reccord == CLOSE_SESSION:
                    bot_say("au revoir")
                    break    
                try:
                    bot_say(MENU_ITEMS_DICT[bot_reccord[0]](bot_reccord[1]))
                except KeyError:
                    continue


