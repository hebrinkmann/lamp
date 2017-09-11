import bibliopixel.colors as colors
from bibliopixel.animation import BaseMatrixAnim
import datetime
import bibliopixel.layout.font as font
import math
import util

class Clock(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(Clock, self).__init__(led, start, end)
        self.minutex = 0
        self.secondx = 0
        self.digitColor = colors.color_scale(colors.White, 16)

    def step(self, amt=1):
        led = self._led
        led.all_off()

        now = util.getNow()

        led.fillScreen(util.getSunColor(now))

        text = str(now.hour)
        (width, height) = font.str_dim(text, '6x4', final_sep = False)
        led.drawText(str(now.hour), x = math.floor((led.width - width) / 2), y = math.floor((led.height - height) / 2), color = self.digitColor, bg = None, font ='6x4')

        self.minutex = self.minutex * .25 + led.width * (now.minute * 60 + now.second) / 3600 * 0.75
        self.secondx = self.secondx * .25 + led.width * now.second / 60 * 0.75

        for x in range(0, led.width):
            for y in range(0, led.height):
                minuteLevel = 96 - (x - self.minutex) * (x - self.minutex) * 60
                if minuteLevel < 0:
                    minuteLevel = 0

                secondLevel = 96 - (x - self.secondx) * (x - self.secondx) * 60
                if (secondLevel < 0):
                    secondLevel = 0

                color = colors.color_blend(colors.color_scale(led.get(x, y), 256 - minuteLevel), colors.color_scale(colors.DarkRed, minuteLevel))
                color = colors.color_blend(colors.color_scale(color, 256 - secondLevel), colors.color_scale(colors.DarkGreen, secondLevel))

                led.set(x, y, color)

        self._step += amt
