import abc


class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    # @abc.abstractclassmethod
    def parse(self):
        pass
