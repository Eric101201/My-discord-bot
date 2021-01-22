import yaml

class yamlhook:
    __slots__ = ['filename']

    def __init__(self, filename):
        self.filename = filename

    # load : 純讀取

    def load(self):
        with open(self.filename, 'r', encoding="utf8") as yd:
            return yaml.safe_load(yd)

    def Operate(self, dictTopic: str, setting):
        with open(self.filename, 'r', encoding="utf8") as yd:
            data = yaml.safe_load(yd)

        data[dictTopic] = setting

        with open(self.filename, 'w', encoding="utf8") as yd:
            yaml.safe_dump(data, yd)