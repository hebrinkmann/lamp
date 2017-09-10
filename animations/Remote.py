from bibliopixel.remote.control import RemoteControl
from ast import literal_eval
import config

class Remote(RemoteControl):
    def __init__(self, layout, animations,
                 external_access=False, port=5000,
                 title='BiblioPixel Remote', bgcolor='black',
                 font_color='white', default=None,
                 triggers=[], auto_demo=None):
        super(Remote, self).__init__(layout, animations, external_access, port, title, bgcolor, font_color, default,
                                     triggers, auto_demo)

        self.handlers['daycolor'] = self.change_daycolor
        self.handlers['nightcolor'] = self.change_nightcolor

    def change_daycolor(self, data):
        try:
            config.daycolor = literal_eval(data)
        except:
            return False, None

        return True, None

    def change_nightcolor(self, data):
        try:
            config.daycolor = literal_eval(data)
        except:
            return False, None

        return True, None