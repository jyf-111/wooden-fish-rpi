from led.ws2812b import Ws2812b
from press.rfp602_ao import Rfp602_ao
from ble.ble import Ble
from config import Config
import time

if __name__ == "__main__":
    config = Config()
    config.load_config()

    ws2812b = Ws2812b(int(config.WS2812B_SIZE), int(config.WS2812B_GPIO))
    ble = Ble(int(config.BLE_PORT))

    min = int(config.RPF602_MIN)
    toggle = int(config.RPF602_TOGGLE)
    max = int(config.RPF602_MAX)
    rfp602_ao = Rfp602_ao((min, toggle, max))

    try:
        i = 0
        txt = config.TXT
        lenth = len(txt)
        while True:
            value = rfp602_ao.read()
            print(value)
            if rfp602_ao.is_pressed():
                ws2812b.set_color((10, 10, 10))
                ble.send(txt[i])
                i += 1
                i %= lenth
            time.sleep(0.01)
            ws2812b.set_color((255, 255, 255))
    except KeyboardInterrupt:
        pass
    finally:
        ws2812b.set_color((0, 0, 0))
