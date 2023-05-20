from woodfish.led.ws2812b import Ws2812b
from rpi_ws281x import Color
import time


def theaterChase(strip, color, wait_ms=50, iterations=10):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=10, iterations=5):
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


if __name__ == "__main__":
    Ws2812b = Ws2812b(60, 18, 255)

    print("Color wipe animations.")
    Ws2812b.set_color((255, 0, 0))  # red wipe
    Ws2812b.set_color((0, 0, 0))
    Ws2812b.set_color((0, 255, 255))  # Blue wipe
    Ws2812b.set_color((0, 0, 0))
    Ws2812b.set_color((255, 0, 255))  # Green wipe
    Ws2812b.set_color((0, 0, 0))

    print("Theater chase animations.")
    print("Rainbow animations.")
    rainbow(Ws2812b.strip)
    Ws2812b.set_color((0, 0, 0))
    rainbowCycle(Ws2812b.strip)
    Ws2812b.set_color((0, 0, 0))
