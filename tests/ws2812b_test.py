from led.ws2812b import ws2812b
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
    ws2812b = ws2812b(60, 18, 255)

    print("Color wipe animations.")
    ws2812b.colorWipe(Color(255, 0, 0))  # red wipe
    ws2812b.colorWipe(Color(0, 0, 0))
    ws2812b.colorWipe(Color(0, 255, 255))  # Blue wipe
    ws2812b.colorWipe(Color(0, 0, 0), 30)
    ws2812b.colorWipe(Color(255, 0, 255))  # Green wipe
    ws2812b.colorWipe(Color(0, 0, 0), 30)

    print("Theater chase animations.")
    print("Rainbow animations.")
    rainbow(ws2812b.getStrip())
    ws2812b.colorWipe(Color(0, 0, 0), 1)
    rainbowCycle(ws2812b.getStrip())
    ws2812b.colorWipe(Color(0, 0, 0), 1)
