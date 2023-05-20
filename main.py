from led.ws2812b import ws2812b
from press.rfp602_ao import rfp602_ao
from ble.ble import ble
import time
from dotenv import load_dotenv, find_dotenv
import os

if __name__ == "__main__":
    load_dotenv(find_dotenv(), override=True)
    TXT = os.getenv("TXT")

    rfp602_ao = rfp602_ao()
    ws2812b = ws2812b(60, 18, 255)
    ble = ble()

    ws2812b.set_color((255, 255, 255))

    i = 0
    try:
        while True:
            value = rfp602_ao.read()
            if rfp602_ao.is_pressed():
                ws2812b.set_color((10, 10, 10))
                ble.send(TXT[i])
                i += 1
                i %= len(TXT)
            time.sleep(0.01)
            ws2812b.set_color((255, 255, 255))
    except KeyboardInterrupt:
        pass
    finally:
        ws2812b.set_color((0, 0, 0))
