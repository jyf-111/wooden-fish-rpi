from led.ws2812b import Ws2812b
from press.rfp602_ao import Rfp602_ao
from keyboard.keyboard import Keyboard
from config import Config
from keyboard.ble import Ble
import random
import asyncio
import logging


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

    def bootstrap(self):
        self.ble.start()
        self.rfp602_ao.start()
        self.keyboard.accept()

    def _map_press_to_light(self, press):
        min_ = int(self.config.RPF602_MIN)
        max_ = int(self.config.RPF602_MAX)
        ret = int((max_ - press) / (max_ - min_) * 255)
        ret = max(ret, 0)
        ret = min(ret, 255)
        return ret

    async def _handle_keyboard(self):
        await self.keyboard.send()

    async def _handle_ws2812b(self):
        color = random.choice(Ws2812b.COLOR)
        brightness = self._map_press_to_light(self.rfp602_ao.current)
        await self.ws2812b.set_color_and_brightness(
            color[0], color[1], color[2], brightness
        )

    async def handle(self):
        while True:
            self.rfp602_ao.event.wait()
            logging.debug("Event received")
            coroutine = [self._handle_keyboard(), self._handle_ws2812b()]
            await asyncio.gather(*coroutine)

            self.rfp602_ao.event.clear()
            logging.debug("Event cleared")

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.handle())
