import json
from os.path import dirname

class Colors(object):
    """all web colors from webcolors.json"""
    with open(dirname(__file__)+"/webcolors.json") as f:
        j = json.load(f)
    colors = { x["name"]:int(x["hex"],16) for x in j }
    rgbs = { x["name"]:(x["rgb"]["r"],x["rgb"]["g"],x["rgb"]["b"]) for x in j }

    @classmethod
    def get(cls,color):
        return cls.colors.get(color, 0xFF69B4)  # HotPink as signal color for missing
    @classmethod
    def rgb(cls,color):
        return cls.rgbs.get(color,(255,105, 180))

def color(color):
    return Colors.get(color)
def rgb(color):
    return Colors.rgb(color)
