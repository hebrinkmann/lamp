import bibliopixel.colors as colors
import datetime
import util

from bibliopixel.animation import BaseMatrixAnim

class SunClock(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(SunClock, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt = 1):
        now = util.getNow()
        startOfDay = util.getStartOfDay(now)

        led = self._led
        showMarker = True
        for x in range(0, led.width):
            for y in range(0, led.height):
                current = startOfDay + datetime.timedelta(days=1) * (x * led.height + y) / led.numLEDs
                color = util.getSunColor(current)

                if showMarker and current >= now:
                    color = colors.color_blend(colors.Red, colors.color_scale(color, 128))
                    showMarker = False

                led.set(x, y, color)

        return
