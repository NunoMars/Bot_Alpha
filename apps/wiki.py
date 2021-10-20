import requests
from bot import listen, speak
# Api Wikipedia


def call_wiki():
    """
    Call Api Wikipedia
    """
    while True:
    # Recherchez un théme à partir de l'entrée utilizateur.*
        speak.bot_say("Que voulez-vous savoir ?")
        title = listen.reccord_audio()
        try:
            s = requests.Session()
            url = "https://fr.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "format": "json",
                "list": "search",
                "srsearch": "{}".format(title)
                }
            r = s.get(url=url, params=params)
            data = r.json()
            page_id = data["query"]["search"][0]["pageid"]
            break
        except:
            speak.bot_say("Je n'ai pas trouvé d'emplacement correspondant à votre demande.")
            speak.bot_say("Veuillez réessayer.")
            continue

    s = requests.Session()

    url = "https://fr.wikipedia.org/w/api.php"
    params = {
        'action': "query",
        'pageids': page_id,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 7,
    }
    r = s.get(url=url, params=params)
    data = r.json()

    return data['query']['pages'][str(page_id)]['extract']