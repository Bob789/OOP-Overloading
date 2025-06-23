from functools import singledispatchmethod

class Logger():

    @singledispatchmethod
    def log(self, message):
        raise NotImplemented("unsupported type")

    @log.register
    def _(self, message: str):
        print(f"Text log = {message}")

    @log.register
    def _(self, message: int):
        print(f"Numeric log {message}")

    @log.register
    def _(self, messages: list):
        for message in messages:
            print(f"List log {message}")