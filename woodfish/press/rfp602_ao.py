from dac.pcf8591 import Pcf8591
from multiprocessing import Event, Process


class Rfp602_ao(Process):
    def __init__(self, min, toggle, max, ns) -> None:
        Process.__init__(self)

        self.__min = min
        self.__toggle = toggle
        self.__max = max

        self.__current = 0
        self.__prev = 0

        self.__pcf8591 = Pcf8591(1, 0x48)

        self.event = Event()

        self.ns = ns

    def _read(self):
        self.__prev = self.__current
        self.__current = self.__pcf8591.read(0)

    def _is_pressed(self):
        return self.__prev >= self.__toggle and self.__current < self.__toggle

    def run(self):
        while True:
            self._read()
            if self._is_pressed():
                self.ns.current = self.__current
                self.event.set()
