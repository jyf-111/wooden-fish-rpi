from rpi_ws281x import PixelStrip


class Ws2812b:
    COLOR = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    # brightness:  Set to 0 for darkest and 255 for brightest
    # frep_hz: LED signal frequency in hertz (usually 800khz)
    # dma: DMA channel to use for generating signal (try 10)
    # invert:  True to invert the signal (when using NPN transistor level shift)
    # channel: set to '30130' for GPIOs 13, 19, 41, 45 or 53
    def __init__(
        self,
        count,
        pin,
        brightness=255,
        frep_hz=800000,
        dma=10,
        invert=False,
        channel=0,
    ):
        self.__strip = PixelStrip(
            count, pin, frep_hz, dma, invert, brightness, channel
        )
        self.__strip.begin()

    def __del__(self):
        for i in range(self.__strip.numPixels()):
            self.__strip.setPixelColorRGB(i, 0, 0, 0)
            self.__strip.show()

    def set_color_and_brightness(self, r=255, g=255, b=255, brightness=255):
        for i in range(self.__strip.numPixels()):
            self.__strip.setPixelColorRGB(i, r, g, b)
            self.__strip.setBrightness(brightness)
            self.__strip.show()

    @property
    def color(self):
        return self.__rgb

    @color.setter
    def color(self, rgb):
        self.__rgb = rgb

    @property
    def brightness(self):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        self.__brightness = brightness
