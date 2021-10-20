from .constants import MENU_ITEMS_DICT, START_SESSION, CLOSE_SESSION


def bot_parser(message):
    """
    Detect a command from the user and return the corresponding words.
    """
    
    list_of_words = message.lower().split()
    print(list_of_words)

    if START_SESSION in list_of_words:
        for word in list_of_words:
            print(word)
            if word in MENU_ITEMS_DICT.keys():
                print(word)
                print(word, " ".join(list_of_words[list_of_words.index(word) + 2:]))
                return word, " ".join(list_of_words[list_of_words.index(word) + 2:])        

    return message