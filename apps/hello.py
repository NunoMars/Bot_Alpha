from random import choice


def say_hello(name):
    salutations = ['Bonjour ', 'Plaisir de te connaître ', 'Salut ', 'Comment vas-tu ']
   
    return choice(salutations) + name + "!"

def introduce(name):
    salutations = ['Bonjour ', 'Plaisir de te connaître ', 'Salut ', 'Comment vas-tu ']
    presentation = " Je me présente a mon tour, je m'appelle Alpha, je suis un robot conversationnel, je suis née le premier septembre 2021, et mon créateur s'appelle Nuno ! Je suis en cours de développement, j'aprends des nouvelles fonctionnalités tous les jours !"

    return choice(salutations) + name + "!" + presentation