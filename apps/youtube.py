import webbrowser


def search_for_video_on_youtube(args):
    """
       YouTube       
    :param args:   
    """

    url = "https://www.youtube.com/results?search_query=" + args
    webbrowser.get().open(url)

    return " Vous avez demandé" + args + "Vois-ci ce que j'ai trouve sur youtube !"