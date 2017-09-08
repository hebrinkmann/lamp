import bibliopixel.colors as colors
from bibliopixel.animation import BaseMatrixAnim

class StripTest(BaseMatrixAnim):
    def __init__(self, led, start=0, end=-1):
        #The base class MUST be initialized by calling super like this
        super(StripTest, self).__init__(led, start, end)
        #Create a color array to use in the animation
        self._colors = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Indigo]

    def step(self, amt=1):
        # Fill the strip, with each sucessive color
        for i in range(self._led.height):
            self._led.set(0, i, self._colors[(self._step + i) % len(self._colors)])
        # Increment the internal step by the given amount
        self._step += amt
