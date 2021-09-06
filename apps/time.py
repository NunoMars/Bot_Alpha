import datetime


def get_time_now():
    """Return current time in string format."""

    week_days = (
        'Lundi',
        'Mardi',
        'Mercredi',
        'Jeudi',
        'Vendredi',
        'Samedi',
        'Dimanche',
    )

    months = (
        'Janvier',
        'Février',
        'Mars',
        'Avril',
        'Mai',
        'Juin',
        'Juillet',
        'Août',
        'Septembre',
        'Octobre',
        'Novembre',
        'Décembre',
    )    

    # datetime object containing current date and time
    now = datetime.datetime.now()

    day = datetime.datetime.now().weekday()
    return [("Aujourd'hui on est le :" + week_days[day] + " " +
    str(now.day) + " " +
    str(months[now.
    month]) + " " +
    str(now.year)), 
    ("Il est " + str(now.hour) +
    " heures et " + str(now.minute) +
    " minutes")]
    
