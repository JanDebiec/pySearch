import string

__author__ = 'jan'

class SpkSpectrum:
    def __init__(self, fileName):
        self.fileName = fileName
        self.data = []
        self.dataSize = 0
        self.avarage = []

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
        self.dataSize = len(self.data)
        for y in range(20):
            self.data[y] = 0
        return self.data

    def movingAverage5(self):
        summa = 0
        # point 0
        i = 0
        summa = 3 * self.data[0] + self.data[1] + self.data[2]
        self.avarage.append(summa / 5)

        # point 1
        i = 1
        summa = summa - self.data[0] + self.data[3]
        self.avarage.append(summa / 5)

        # point 2
        i = 2
        summa = summa - self.data[0] + self.data[4]
        self.avarage.append(summa / 5)

        # points from 3 till size - 3
        i = 3
        while i < (self.dataSize - 2):
            summa = summa - self.data[i - 3] + self.data[i + 2]
            self.avarage.append(summa / 5)
            i = i + 1

        # point size - 2
        summa = summa - self.data[i - 3] + self.data[self.dataSize - 1]
        self.avarage.append(summa / 5)
        i = i + 1

        # point size - 1
        summa = summa - self.data[i - 3] + self.data[self.dataSize - 1]
        self.avarage.append(summa / 5)
        i = i + 1

        return self.avarage
