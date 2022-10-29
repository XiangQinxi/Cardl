from os import getenv, environ
from json import dumps, loads

EnvDefault = "{}"
EnvName = "Cardi.json"

def get_key():
    return loads(environ.get(EnvName))

def set_key(json: str) -> None:
    environ[EnvName] = Strings

def set(key_name: str, key_value: str) -> None:
    Value = loads(environ[EnvName])
    Value[key_name] = key_value
    environ[EnvName] = dumps(Value)

def set_default(key_name: str, key_value: str) -> None:
    environ.setdefault(key_name, key_value)

def get(key_name: str) -> str:
    return loads(environ.get(EnvName))[KeyName]

set_default(EnvName, EnvDefault)


class CObject:
    @property
    def key(self) -> dict:
        return get_key()

    @key.setter
    def key(self, Json: str) -> None:
        set_key(Json)

    def set(self, KeyName: str, KeyValue: str) -> None:
        set(KeyName, KeyValue)

    def setDefault(self, KeyName: str, KeyValue: str) -> None:
        set_default(KeyName, KeyValue)

    def get(self, KeyName: str) -> str:
        return get(KeyName)

    def hex(self, hex: str):
        from ctypes.wintypes import RGB
        from PIL import ImageColor
        color = ImageColor.getcolor(hex, "RGB")
        return RGB(color[0], color[1], color[2])

    def rgb(self, red: int, green: int, blue: int):
        from ctypes.wintypes import RGB
        return RGB(red, green, blue)