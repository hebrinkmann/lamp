import bibliopixel.colors as colors
import datetime
import math
import util

from bibliopixel.animation import BaseMatrixAnim

class SunClock(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(SunClock, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
        now = datetime.datetime.now()
        startOfDay = datetime.datetime(now.year, now.month, now.day)

        for i in range(0, self._led.height):
            current = startOfDay + datetime.timedelta(days=1) * i / self._led.height
            color = util.getSunColor(current)
            self._led.set(0, i, color)

        indexNow = math.floor((now - startOfDay) * self._led.height / datetime.timedelta(days=1))
        color = self._led.get(0, indexNow)
        self._led.set(0, indexNow, colors.color_blend(colors.Red, colors.color_scale(color, 128)))

        return
