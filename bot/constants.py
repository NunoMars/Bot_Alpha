from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki


MENU_ITEMS =["alpha", "météo", "jouer", "heure", "date", "wikipedia"]

MENU_ITEMS_DICT = {
    "date" : get_time_now()[0],
    "jour" : get_time_now()[0],
    "heure" : get_time_now()[1],
    "météo" : weather_forecast,
    "jouer" :"Je pourrait bientôt le faire .. je j'aprends tous les jours !",
    "wikipedia" : call_wiki,
    "error" : "Je n'ai pas compris votre demande, veuillez réessayer",
}

START_SESSION = "alpha"
CLOSE_SESSION = "au revoir alpha"