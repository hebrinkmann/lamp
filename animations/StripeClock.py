import bibliopixel.colors as colors
from bibliopixel.animation import BaseMatrixAnim
import util
import datetime
import math
import config

class StripeClock(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(StripeClock, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt=1):
        now = util.getNow()

        led = self._led
        led.fillScreen(util.getSunColor(now))

        y = math.floor(led.height * now.minute / 60)
        led.drawLine(0, y, led.width, y, config.minutecolor)