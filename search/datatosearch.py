__author__ = 'jan'


class DataToSearch:
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.end = len(data)
        self.actStart = 0
        self.actEnd = 0
        self.peaks = []

    def level0(self):
        self.actStart = 0
        self.actEnd = self.end
        peak = peak.peak
        self.peaks.append(peak)
        self.searchToRight(0, -1)



    def searchToLeft(self, indexToFind, indexToUpdate):
        pass


    def searchToRight(self, indexToFind, indexToUpdate):
        pass