import ephem as ep
import bibliopixel.colors as colors
import config
import datetime
from dateutil.tz import *

def getNow():
    return datetime.datetime.now(tzlocal())

def getStartOfDay(date):
    return datetime.datetime(date.year, date.month, date.day, tzinfo = date.tzinfo)

def getSunColor(date):
    utc_dt = date.astimezone(tzutc())
    startOfDay_dt = getStartOfDay(date)
    startOfDay_utc_dt = startOfDay_dt.astimezone(tzutc())

    current = ep.Date((utc_dt.year, utc_dt.month, utc_dt.day, utc_dt.hour, utc_dt.minute, utc_dt.second))
    startOfDay = ep.Date((startOfDay_utc_dt.year, startOfDay_utc_dt.month, startOfDay_utc_dt.day, startOfDay_utc_dt.hour, startOfDay_utc_dt.minute, startOfDay_utc_dt.second))
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
