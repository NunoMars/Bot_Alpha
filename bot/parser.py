from .constants import MENU_ITEMS_DICT, START_SESSION


def bot_parser(message):
    """
    Detect a command from the user and return the corresponding words.
    """
    
    list_of_words = message.lower().split()

    if START_SESSION in list_of_words:
        list_of_words.remove(START_SESSION)
        for word in list_of_words:
            if word in MENU_ITEMS_DICT.keys():
                return word, " ".join(list_of_words[list_of_words.index(word) + 2:])        
