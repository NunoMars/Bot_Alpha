from bot.speak import bot_say
from bot.listen import reccord_audio
from  meteofrance_api  import  MeteoFranceClient


def  weather_forecast():
    """Testez l'utilisation du workflow classique avec la bibliothèque Python."""
    # Initier le client
    client  =  MeteoFranceClient()
    #le bot demande la ville
    bot_say("vous voulez la météo sur quelle ville?")
    #récupérer la ville    
    while True:
        bot_reccord = reccord_audio()
        if bot_reccord["success"] == True:
            choice = bot_reccord["transcription"]
            bot_say("Vous avez dit : " + choice )            
            place = choice.lower()
            print("Vous avez choisi " + place)
            break
        else:
            bot_say("je n'ai pas compris, vous voulez la météo sur quelle ville?")
            continue
    # Recherchez un emplacement à partir du nom.
    list_places  =  client.search_places ( place )
    print(list_places)
    my_place  =  list_places [ 0 ]
    print ( 'Place:', my_place)
    # Récupérer les prévisions météo pour l'emplacement
    my_place_weather_forecast  =  client.get_forecast_for_place( my_place)

    # Obtenez les prévisions quotidiennes
    my_place_daily_forecast  =  my_place_weather_forecast . daily_forecast
    print(my_place_daily_forecast[0])

    # Affichage des prévisions quotidiennes
    bot_say("Aujourd'hui sur ..." + my_place.name + "..." +
        "le temps est : " + str(my_place_daily_forecast[0]['weather12H']['desc']) +
        "les températures minima et maxima sont : " + str(my_place_daily_forecast[0]['T']['min']) + "... et " + str(my_place_daily_forecast[0]['T']['max']) +
        "le taux d'humidité est de. " + str(my_place_daily_forecast[0]['humidity']['min']) + "... et " + str(my_place_daily_forecast[0]['humidity']['max']) + "."
    )
    # Si la prévision de pluie dans l'heure est disponible, obtenez-la.
    if  my_place_weather_forecast . position [ "rain_product_available" ] ==  1 :
        my_place_rain_forecast  =  client . get_rain ( my_place.latitude , my_place.longitude )
        next_rain_dt  =  my_place_rain_forecast . next_rain_date_locale ()
        if  not  next_rain_dt :
            rain_status  =  "Pas de pluie prévue dans l'heure suivante."
        else :
            rain_status  =  next_rain_dt . strftime ( "%H:%M" )
    else :
        rain_status  =  "Aucune prévision de pluie disponible."
  
    bot_say(rain_status)
    return False



if __name__  ==  "__main__" :
    weather_forecast()
