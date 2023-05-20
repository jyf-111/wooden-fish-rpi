from dac.pcf8591 import Pcf8591


class Rfp602_ao:
    def __init__(self, range) -> None:
        self.range = range
        self.pcf8591 = Pcf8591(1, 0x48)
        self.current = 0
        self.prev = 0

    def read(self):
        self.prev = self.current
        self.current = self.pcf8591.read(0)
        return self.current

    def map_to_light(self):
        range = self.range
        if self.current < range[0]:
            return 0
        precent = (self.current * 1.0 - range[0]) / (range[2] - range[0])
        return int(precent * range[2])

    def is_pressed(self):
        return self.prev >= self.range[1] and self.current < self.range[1]
