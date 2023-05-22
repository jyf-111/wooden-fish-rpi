from config import Config


class Content:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.TXT = Config().TXT
        self.idx = 0
        self.length = len(self.TXT)

    def get_next_char(self):
        char = self.TXT[self.idx]
        self.idx = self.idx + 1
        self.idx = self.idx % self.length
        return char
