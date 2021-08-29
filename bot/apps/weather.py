from  meteofrance_api  import  MeteoFranceClient

from geopy.geocoders import Nominatim 

def geolocate():
  
    geoLoc = Nominatim(user_agent="GetLoc") 
  
    locname = geoLoc.reverse("26.7674446, 81.109758") 
    
    print(locname.address) 


def  weather_forecast ():
    """Testez l'utilisation du workflow classique avec la bibliothèque Python."""
    # Initier le client
    client  =  MeteoFranceClient()

    # Recherchez un emplacement à partir du nom.
    list_places  =  client.search_places ( 'Pontoise' )
    my_place  =  list_places [ 0 ]
    print ( 'Place:', my_place )
    # Récupérer les prévisions météo pour l'emplacement
    my_place_weather_forecast  =  client.get_forecast_for_place( my_place)

    # Obtenez les prévisions quotidiennes
    my_place_daily_forecast  =  my_place_weather_forecast . daily_forecast
    print(my_place_daily_forecast)
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
  
    print(rain_status)



if __name__  ==  "__main__" :
    weather_forecast()
    geolocate()