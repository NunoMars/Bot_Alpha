from .constants import MENU_ITEMS_DICT, START_SESSION, CLOSE_SESSION


def bot_parser(message):
    """
    Detect a command from the user and return the corresponding words.
    """
    
    list_of_words = message.lower().split()

    if message in [START_SESSION, CLOSE_SESSION]:
        print(message)
        return message

    print(list_of_words)

    for item in list_of_words:
        if item in MENU_ITEMS_DICT.keys():
            return item, " ".join(list_of_words[list_of_words.index(item) + 2:])          

    return None