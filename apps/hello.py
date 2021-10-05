from random import choice
from bot.speak import bot_say


def say_hello(name):
    salutations = ['Bonjour ', 'Plaisir de te connaître ', 'Salut ', '', 'Comment vas-tu ']
    presentation = " Je me présente a mon tour, je m'appelle Alpha, je suis un robot conversationnel, je suis née le premier septembre 2021, et mon créateur s'appel Nuno !"

    return choice(salutations) + name + "!" + presentation

