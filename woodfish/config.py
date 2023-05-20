from dotenv import load_dotenv, find_dotenv
import os
import io
import logging


class Config:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def load_config(self):
        load_dotenv(find_dotenv(), override=True)
        self.FILENAME = os.getenv("FILENAME")
        with io.FileIO(self.FILENAME) as f:
            self.TXT = f.read().decode()

        self.WS2812B_SIZE = os.getenv("WS2812B_SIZE")
        self.WS2812B_GPIO = os.getenv("WS2812B_GPIO")

        self.BLE_PORT = os.getenv("BLE_PORT")

        self.RPF602_MIN = os.getenv("RPF602_MIN")
        self.RPF602_MAX = os.getenv("RPF602_MAX")
        self.RPF602_TOGGLE = os.getenv("RPF602_TOGGLE")
        self.LOG = os.getenv("LOG")

    def config_logging(self):
        levels = {
            "critical": logging.CRITICAL,
            "error": logging.ERROR,
            "warn": logging.WARNING,
            "warning": logging.WARNING,
            "info": logging.INFO,
            "debug": logging.DEBUG,
        }
        logging.basicConfig(
            format="[%(asctime)s %(name)s:%(levelname)s] %(message)s",
            datefmt="%d-%M-%Y %H:%M:%S",
            level=levels.get(self.LOG.lower(), logging.INFO),
        )
        current_level = logging.getLogger().getEffectiveLevel()
        level_name = logging.getLevelName(current_level)
        logging.info("log level %s", level_name)
