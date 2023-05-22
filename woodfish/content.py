from config import Config
import pinyin


class Content:
    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        self.filename = Config().FILENAME
        self.idx = 0

    def load_content(self):
        file_list = []
        if self.filename is None:
            from os import walk

            for dir_path, dir_names, file_names in walk("woodfish"):
                for file in file_names:
                    if not file.endswith(".pyc"):
                        file_list.append(f"{dir_path}/{file}")
        else:
            file_list.append(self.filename)

        self.content = ""
        self.length = 0

        for file in file_list:
            with open(file, "r") as f:
                content = f.read()
                content = pinyin.get(content, format="strip").translate(
                    {
                        ord(f): ord(t)
                        for f, t in zip(
                            """，。！？【】（）％＃＠＆１２３４５６７８９
                            ０", ",.!?[]()%#@&1234567890"""
                        )
                    }
                )
                content += "\n"
                self.content += content
                self.length += len(self.content) + 1

    def get_next_char(self):
        char = self.content[self.idx]
        self.idx = self.idx + 1
        self.idx = self.idx % self.length
        return char
