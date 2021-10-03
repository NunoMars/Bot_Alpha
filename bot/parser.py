from .constants import MENU_ITEMS


def bot_parser(message):
    """
    Detect a command from the user and return the corresponding words.
    """
    list_of_words = message.lower().split()

    for item in list_of_words:
        if item  not in MENU_ITEMS:
            return None            
        else:
            return " ".join(list_of_words[list_of_words.index(item) + 2:])