from led.ws2812b import ws2812b
from dac.pcf8591 import pcf8591
import time


def value(input):
    if input < 200:
        return 0
    pre = input / 256.0
    pre = (int)(pre * 56) + 200
    return pre


if __name__ == "__main__":
    pcf8591 = pcf8591(1, 0x48)
    ws2812b = ws2812b(60, 18, 255)

    ws2812b.set_color((255, 255, 255))

    try:
        while True:
            input = pcf8591.read(0)
            print("{}".format(input))
            ws2812b.set_brightness(value(input))
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        ws2812b.set_color((0, 0, 0))
