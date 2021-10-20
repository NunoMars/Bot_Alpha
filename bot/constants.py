from apps.weather import weather_forecast
from apps.time import get_time_now
from apps.wiki import call_wiki
from apps.youtube import search_for_video_on_youtube
from apps.hello import say_hello
from bot import listen, speak


MENU_ITEMS_DICT = {
    "bonjour" : say_hello,
    ("date", "jour") : get_time_now()[0],
    ("heure", "l'heure"): get_time_now()[1],
    "météo" : weather_forecast(listen, speak),
    "jouer" :"Je pourrait bientôt le faire .. je j'aprends tous les jours !",
    ("propos", "parle", "a propos") : call_wiki(listen, speak),
    ("youtube", "video"): search_for_video_on_youtube(listen, speak),
    "error" : "Je n'ai pas compris votre demande, veuillez réessayer",
}

START_SESSION = "alpha"
CLOSE_SESSION = "au revoir alpha"