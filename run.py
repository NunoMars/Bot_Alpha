# coding: utf-8
from menu import bot_menu, bot_say, reccord_audio


def start():
    bot_say("Bonjour... session initialisée... que puis-je faire pour vous?")
    while True:
        bot_menu()
        break

if __name__ == '__main__':
    start()