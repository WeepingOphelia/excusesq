import random
import requests

datamuse = "https://api.datamuse.com/words?"

class Excuse():
    def __init__(self):
        self.text = ""
        self.libs = []
        self.template = ""
        pass

    def set_text(self):
        pass

class DefaultExcuse(Excuse):
    def __init__(self):
        super().__init__()
        self.template = "My ? is full of ?."
        self.libs = [{"api": datamuse, "affix": "lc=my&rc=is&ml=hovercraft&pos=n"}, {"api": datamuse, "affix": "lc=many&ml=eels&pos=n"}]

    def set_text(self):
        pass