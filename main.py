# coding: utf-8
from menu import bot_menu, bot_say


def start():
    bot_say("Bonjour... session initialisée...")
    while True:
        bot_menu()


if __name__ == '__main__':
    start()