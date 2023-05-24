from led.ws2812b import Ws2812b
from press.rfp602_ao import Rfp602_ao
from keyboard.keyboard import Keyboard
from config import Config
from keyboard.ble import Ble
import random


class Core:
    def __init__(self):
        self.config = Config()
        self.config.load_config()
        self.config.config_logging()

        ws2812b_size = int(self.config.WS2812B_SIZE)
        ws2812b_gpio = int(self.config.WS2812B_GPIO)
        self.ws2812b = Ws2812b(ws2812b_size, ws2812b_gpio)

        self.ble = Ble()
        self.keyboard = Keyboard()

        min = int(self.config.RPF602_MIN)
        toggle = int(self.config.RPF602_TOGGLE)
        max = int(self.config.RPF602_MAX)
        self.rfp602_ao = Rfp602_ao(min, toggle, max)

        self.rfp602_ao.keyboard = self.keyboard
        self.rfp602_ao.ws2812b = self.ws2812b

    def _map_press_to_light(self, press):
        min = int(self.config.RPF602_MIN)
        max = int(self.config.RPF602_MAX)
        return int((max - press) / (max - min) * 255)

    def run(self):
        component = [self.ble, self.keyboard, self.rfp602_ao]

        [item.start() for item in component]

        while True:
            rfp602_ao = self.rfp602_ao
            rfp602_ao.event.wait()

            keyboard = self.keyboard
            keyboard.event.set()

            ws2812b = self.ws2812b
            ws2812b.color = random.choice(Ws2812b.COLOR)
            ws2812b.brightness = self._map_press_to_light(rfp602_ao.current)
            ws2812b.show()

            rfp602_ao.event.clear()
