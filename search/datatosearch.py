__author__ = 'jan'


class DataToSearch:
    def __init__(self, data, peakSeparation = 6):
        self.data = data
        self.start = 0
        self.end = len(data)
        self.actStart = 0
        self.actEnd = 0
        self.peaks = []
        self.peakSeparation = peakSeparation

    def level0(self):
        self.actStart = 0
        self.actEnd = self.end
        peak = peak.peak
        self.peaks.append(peak)
        self.firstSearchToRight(0)



    def searchToLeft(self, indexToFind, indexToUpdate):
        pass


    def firstSearchToRight(self):
        '''
        first search, we can start from low values,
        we don't need to check if we go down.
        After search, peak must be validating,
        if the peak is far away from he borders.
        As result preak[0] will be filled .
        :return: -1 if not found, 0 by OK
        '''
        i = 0
        maxValue = 0
        maxPosition = -1
        for value in self.data:
            if value > maxValue:
                maxValue = value
                maxPosition = i
            i = i + 1
        valid = self.validatePeak(maxPosition)
        if valid:
            self.peaks[0].maxPosition = maxPosition
            self.peaks[0].maxValue = maxValue
            return 0
        else:
            return -1



    def validatePeak(selfposition):
        '''


        :rtype : bool
        :param selfposition:
        :return: bool, True if valid
        '''
        return True


    def searchToRight(self, indexToFind, indexToUpdate):
        pass