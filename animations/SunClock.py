import bibliopixel.colors as colors
import ephem as ep
import datetime
import math

from bibliopixel.animation import BaseStripAnim

class SunClock(BaseStripAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(SunClock, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
        now = datetime.datetime.now()
        startOfDay = datetime.datetime(now.year, now.month, now.day)

        for i in range(0, self._led.numLEDs):
            current = startOfDay + datetime.timedelta(days=1) * i / self._led.numLEDs
            color = self.getColor(current)
            self._led.set(i, color)

        indexNow = math.floor((now - startOfDay) * self._led.numLEDs / datetime.timedelta(days=1))
        color = self._led.get(indexNow)
        self._led.set(indexNow, colors.color_blend(colors.Red, colors.color_scale(color, 128)))

        return

    def getColor(self, date):
        current = ep.Date((date.year, date.month, date.day, date.hour, date.minute, date.second))
        startOfDay = ep.Date((date.year, date.month, date.day))
        endOfDay = startOfDay + 1

        observer = ep.Observer()
        observer.lat = '54.0'
        observer.lon = '-10.0'
        observer.date = startOfDay
        sunrise = observer.next_rising(ep.Sun())
        sunset = observer.next_setting(ep.Sun())

        result = colors.Black

        if (current >= startOfDay) & (current < endOfDay):
            result = colors.Blue

            if (current >= sunrise) & (current < sunset):
                result = colors.Yellow

        return result

