from bot.speak import bot_say
from bot.listen import reccord_audio
from bot.constants import CLOSE_SESSION, MENU_ITEMS_DICT


def bot_menu():
    """app menu"""
    bot_say("j'écoute...")
    while True:#Main loop
        bot_reccord = reccord_audio()

        if bot_reccord is None:
            continue               
            
        elif bot_reccord == CLOSE_SESSION:#close cession and continue listening
            bot_say("au revoir")
            break

        try:
            print(MENU_ITEMS_DICT[bot_reccord[0]](bot_reccord[1]))
            bot_say(MENU_ITEMS_DICT[bot_reccord[0]](bot_reccord[1]))
            continue
        except (KeyError):
            print("Ups... pour continuer dites Alpha!")
            continue


if __name__ == "__main__":
    bot_menu()