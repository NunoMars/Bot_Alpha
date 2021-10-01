import requests

# Api Wikipedia


def call_wiki(title="Ratatouille"):
    """
    Call Api Wikipedia
    """
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

    text = data['query']['pages'][str(page_id)]['extract']
    return text