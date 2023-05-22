from led.ws2812b import Ws2812b
from press.rfp602_ao import Rfp602_ao
from keyboard.keyboard import Keyboard
from config import Config
import logging
from content import Content


class Core:
    def init_config(self):
        self.config = Config()
        self.config.load_config()
        self.config.config_logging()

    def init_ws2812b(self):
        logging.info("init ws2812b")

        ws2812b_size = int(self.config.WS2812B_SIZE)
        ws2812b_gpio = int(self.config.WS2812B_GPIO)
        self.ws2812b = Ws2812b(ws2812b_size, ws2812b_gpio)

    def init_keyboard(self):
        logging.info("init keyboard")

        self.keyboard = Keyboard()
        self.keyboard.bootstrap()

        logging.info("wait for keyboard accept")
        self.keyboard.accept()
        logging.info("keyboard accepted")

    def init_rfp602_ao(self):
        logging.info("init rpf602_ao")

        min = int(self.config.RPF602_MIN)
        toggle = int(self.config.RPF602_TOGGLE)
        max = int(self.config.RPF602_MAX)
        self.rfp602_ao = Rfp602_ao((min, toggle, max))

    def run(self):
        ws2812b = self.ws2812b
        keyboard = self.keyboard
        rfp602_ao = self.rfp602_ao
        content = Content()
        content.load_content()

        while True:
            value = rfp602_ao.read()
            logging.debug("press value %d", value)

            if rfp602_ao.is_pressed():
                keyboard.send(content.get_next_char())
                logging.debug("send")

                ws2812b.set_color(10, 10, 10)

            ws2812b.set_color(255, 255, 255)
