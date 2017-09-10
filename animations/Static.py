from bibliopixel.animation import BaseMatrixAnim
import util

class Static(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        super(Static, self).__init__(led, start, end)

    def step(self, amt=1):
        self._led.fillScreen(util.getSunColor(util.getNow()))