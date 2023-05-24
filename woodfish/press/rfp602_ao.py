from dac.pcf8591 import Pcf8591
from threading import Event, Thread
import logging


class Rfp602_ao(Thread):
    def __init__(self, min, toggle, max) -> None:
        Thread.__init__(self)
        self.daemon = True

        self.__min = min
        self.__toggle = toggle
        self.__max = max

        self.__current = 0
        self.__prev = 0

        self.__pcf8591 = Pcf8591(1, 0x48)

        self.event = Event()

    def _read(self):
        self.__prev = self.__current
        self.__current = self.__pcf8591.read(0)

    def _is_pressed(self):
        return self.__prev >= self.__toggle and self.__current < self.__toggle

    def run(self):
        while True:
            self._read()
            logging.debug(self.__current)
            if self._is_pressed():
                self.event.set()

    @property
    def current(self):
        return self.__current

    @property
    def prev(self):
        return self.__prev
