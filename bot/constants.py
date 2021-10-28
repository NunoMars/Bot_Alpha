from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki
from apps.youtube import search_for_video_on_youtube
from apps.hello import say_hello, introduce
from bot.get_gps import get_gps_position


MENU_ITEMS_DICT = {
    "bonjour" : say_hello,
    "présente" : introduce,
    "date" : get_time_now()[0],
    "jour" : get_time_now()[0],
    "l'heure" : get_time_now()[1],
    "heure" : get_time_now()[1],
    "météo" : weather_forecast,
    "jouer" :"Je pourrait bientôt le faire .. je j'aprends tous les jours !",
    "a propos" : call_wiki,
    "propos" : call_wiki,
    "parle" : call_wiki,
    "video" : search_for_video_on_youtube,
    "youtube" : search_for_video_on_youtube,
    "error" : "Je n'ai pas compris votre demande, veuillez réessayer",
}

START_SESSION = "alpha"
CLOSE_SESSION = "au revoir alpha"