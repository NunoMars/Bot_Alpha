from bot.speak import bot_say
from bot.listen import reccord_audio
from apps.weather import weather_forecast


def bot_menu():
    menu_items =["météo", "jouer"]
    
    while True:
        bot_reccord = reccord_audio()
        
        choice = bot_reccord["transcription"].lower()
        print(choice)

        test_in_list = bot_reccord["transcription"].split()
        print(test_in_list)

        if bot_reccord["success"] == True:
            if 'menu' in test_in_list:
                print("ok menu")
                bot_say("Ok, voilà ce que je sais déja faire ..." + str([i for i in menu_items]) + ".")
                return True

            if "météo" in test_in_list:
                weather_forecast()
                return True

            if "session" in test_in_list:
                bot_say("ok je ferme la session!")
                return False
        else :
            bot_say(bot_reccord["transcription"])
            bot_say("Pour connaitre la liste de ce que je sais déja faire... dites Menu")
            continue
