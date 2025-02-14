import random
import requests

datamuse = "https://api.datamuse.com/words?"

import random  

templates = [  
    "My {noun} is full of {nouns}.",  
    "I couldn't {verb} because my {noun} was {verbing}.",  
    "A {adj} {noun} {verbed} my {noun}, so I had to {verb}.",  
    "I was on my way, but a {adj} {noun} blocked the {noun}.",  
    "By the time I finished {verbing} my {noun}, it was already too late."  
]


class Excuse():
    def __init__(self):
        self.text = ""
        self.template = random.choice(templates)
        pass

    def set_text(self):
        pass

class DefaultExcuse(Excuse):
    def __init__(self):
        super().__init__()
        self.template = "My {0} is full of {1}."
        self.libs = [{"api": datamuse, "affix": "lc=my&rc=is&ml=hovercraft&pos=n"}, {"api": datamuse, "affix": "lc=many&ml=eels&pos=n"}]

    def set_text(self):
        pass