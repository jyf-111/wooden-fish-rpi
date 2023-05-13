import time
from rpi_ws281x import PixelStrip, Color


class ws2812b:
    # brightness:  Set to 0 for darkest and 255 for brightest
    # frep_hz: LED signal frequency in hertz (usually 800khz)
    # dma: DMA channel to use for generating signal (try 10)
    # invert:  True to invert the signal (when using NPN transistor level shift)
    # channel: set to '30130' for GPIOs 13, 19, 41, 45 or 53
    def __init__(
        self, count, pin, brightness, frep_hz=800000, dma=10, invert=False, channel=0
    ):
        # Create NeoPixel object with appropriate configuration.
        self.strip = PixelStrip(count, pin, frep_hz, dma, invert, brightness, channel)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def __del__(self):
        self.colorWipe(Color(0, 0, 0))

    def colorWipe(self, color, wait_ms=20):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms / 1000.0)

    def getStrip(self):
        return self.strip
