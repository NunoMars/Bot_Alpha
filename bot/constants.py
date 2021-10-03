from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki


MENU_ITEMS =["météo", "jouer", "heure", "l'heure", "date", "jour", "propos", "parle", "a propos"]

MENU_ITEMS_DICT = {
    "date" : get_time_now()[0],
    "jour" : get_time_now()[0],
    "l'heure" : get_time_now()[1],
    "heure" : get_time_now()[1],
    "météo" : weather_forecast,
    "jouer" :"Je pourrait bientôt le faire .. je j'aprends tous les jours !",
    "propos" : call_wiki,
    "a propos" : call_wiki,
    "parle" : call_wiki,
    "error" : "Je n'ai pas compris votre demande, veuillez réessayer",
}

START_SESSION = "alpha"
CLOSE_SESSION = "au revoir alpha"