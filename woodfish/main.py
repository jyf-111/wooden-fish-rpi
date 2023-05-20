from led.ws2812b import Ws2812b
from press.rfp602_ao import Rfp602_ao
from ble.ble import Ble
from config import Config
import time
import logging

if __name__ == "__main__":
    config = Config()
    config.load_config()
    config.config_logging()

    logging.info("load config")

    ws2812b_size = int(config.WS2812B_SIZE)
    ws2812b_gpio = int(config.WS2812B_GPIO)
    ws2812b = Ws2812b(ws2812b_size, ws2812b_gpio)

    logging.info("init ws2812b")

    ble_port = int(config.BLE_PORT)
    ble = Ble(ble_port)
    ble.accept()

    logging.info("init bluetooth")

    min = int(config.RPF602_MIN)
    toggle = int(config.RPF602_TOGGLE)
    max = int(config.RPF602_MAX)
    rfp602_ao = Rfp602_ao((min, toggle, max))

    logging.info("init rpf602")

    try:
        i = 0
        txt = config.TXT
        lenth = len(txt)
        while True:
            value = rfp602_ao.read()
            logging.debug("press value %d", value)

            if rfp602_ao.is_pressed():
                ws2812b.set_color(10, 10, 10)
                logging.debug("ws2812b set color")
                ble.send(txt[i])
                logging.debug("ble send %s", txt[i])
                i += 1
                i %= lenth

            time.sleep(0.01)

            ws2812b.set_color(255, 255, 255)
            logging.debug("ws2812b set color")
    except KeyboardInterrupt:
        logging.warning("KeyboardInterrupt")
        pass
    finally:
        ws2812b.set_color(0, 0, 0)
        logging.debug("ws2812b set color")
