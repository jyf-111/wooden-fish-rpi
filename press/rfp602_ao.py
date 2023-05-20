from dac.pcf8591 import pcf8591


class rfp602_ao:
    def __init__(self) -> None:
        self.pcf8591 = pcf8591(1, 0x48)
        self.current = 0
        self.prev = 0

    def read(self):
        self.prev = self.current
        self.current = self.pcf8591.read(0)
        return self.current

    def map(self):
        if self.current < 100:
            return 0
        precent = (self.current * 1.0 - 100) / (256 - 100)
        return int(precent * 256)

    def is_pressed(self):
        if self.prev >= 250 and self.current < 250:
            return True
        else:
            return False
