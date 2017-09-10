import ephem as ep
import bibliopixel.colors as colors
import config

def getSunColor(date):
    current = ep.Date((date.year, date.month, date.day, date.hour, date.minute, date.second))
    startOfDay = ep.Date((date.year, date.month, date.day))
    endOfDay = startOfDay + 1

    observer = ep.Observer()
    observer.lat = '54.0'
    observer.lon = '10.0'
    observer.date = startOfDay
    sunrise = observer.next_rising(ep.Sun())
    sunset = observer.next_setting(ep.Sun())

    result = colors.Black

    if (current >= startOfDay) & (current < endOfDay):
        result = config.nightcolor

        if (current >= sunrise) & (current < sunset):
            result = config.daycolor

    return result
