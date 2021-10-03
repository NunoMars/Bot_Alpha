from .constants import MENU_ITEMS, START_SESSION, CLOSE_SESSION


def bot_parser(message):
    """
    Detect a command from the user and return the corresponding words.
    """
    print(message)
    list_of_words = message.lower().split()
    print(list_of_words)

    if message in [START_SESSION, CLOSE_SESSION]:
        return message

    for item in list_of_words:
        if item not in MENU_ITEMS:
            return None            

        return item, " ".join(list_of_words[list_of_words.index(item) + 2:])