import string

__author__ = 'jan'

class SpkSpectrum:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = []

    def read(self, limit):
        with open(self.fileName) as f:
            lines = f.readlines()
        i = 0
        for line in lines:
            # skip first 5 lines
            if (i > 5) and (i < limit):
                value = string.atoi(line)
                self.data.append(value)
            i = i + 1
        return self.data


