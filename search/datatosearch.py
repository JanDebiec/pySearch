# from search import spectrumpeak

__author__ = 'jan'

class SpectrumPeak:
    def __init__(self):
        self.maxValue = 0
        self.maxPosition = -1
        self.leftBorder = -1
        self.leftBorderValue = 0
        self.rightBorder = -1
        self.rightBorderValue = 0
        self.valid = False

class DataToSearch:
    def __init__(self, data, peakSeparation = 6):
        self.data = data
        self.start = 0
        self.end = len(data)
        self.actStart = 0
        self.actEnd = 0
        self.peaks = []
        self.peakSeparation = peakSeparation
        self.valid0 = -1
        self.valid1 = -1

    def level0(self):
        '''
        searching first highest peak,

        from start to end

        :return: 0 if peak found and validated
        '''
        self.actStart = 0
        self.actEnd = self.end
        peak = SpectrumPeak()
        self.peaks.append(peak)
        self.valid0 = self.firstSearchToRight()
        if self.valid0 == 0: # ok
            return 0
        else:
            return -1

    def level1(self):
        '''
        searching 2 next peaks,

        first from max left to start,
        second from max to end
        after finding, the peaks will be compared
        to find the second hghest

        :return: 0 if the minimas for the peak0 are found
        independet if the second or third peaks are validated
        '''

        # search from peak0 to left, to start
        self.actStart = self.peaks[0].maxPosition
        self.actEnd = self.start
        validL = self.searchToLeft(1, 0)

        # search from peak0 to right, to end
        self.actStart = self.peaks[0].maxPosition
        self.actEnd = self.end
        validLR = self.searchToRight(2, 0)

        return validL

    def searchToLeft(self, indexToFind, indexToUpdate):
        peak = SpectrumPeak()
        self.peaks.append(peak)
        retValue = -1
        i = self.actStart
        maxValue = 0
        maxPosition = -1
        firstMinimum = self.peaks[indexToUpdate].maxValue
        firstMinimumPosition = self.peaks[indexToUpdate].maxPosition
        firstMinimumFound = False
        while i > self.actEnd:
            value = self.data[i]
            if not firstMinimumFound:
                if value <= firstMinimum:
                    firstMinimum = value
                    firstMinimumPosition = i
                else:
                    firstMinimumFound = True
                    retValue = 0
            else:
                if value > maxValue:
                    maxValue = value
                    maxPosition = i
            i = i - 1
        valid = self.validatePeak(maxPosition)
        if valid:
            self.peaks[indexToFind].maxPosition = maxPosition
            self.peaks[indexToFind].maxValue = maxValue
            self.peaks[indexToFind].valid = True
        return retValue


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
            self.peaks[0].valid = True
            return 0
        else:
            return -1



    def validatePeak(self, position):
        '''
        check if position of peak, far enough from the search borders

        :param selfposition:
        :rtype : bool
        :return: bool, True if valid
        '''
        if (position - self.actStart) < self.peakSeparation:
            return False
        if (self.actEnd - position) < self.peakSeparation:
            return False
        return True


    def searchToRight(self, indexToFind, indexToUpdate):
        peak = SpectrumPeak()
        self.peaks.append(peak)
        retValue = -1
        i = self.actStart
        maxValue = 0
        maxPosition = -1
        firstMinimum = self.peaks[indexToUpdate].maxValue
        firstMinimumPosition = self.peaks[indexToUpdate].maxPosition
        firstMinimumFound = False
        while i < self.actEnd:
            value = self.data[i]
            if not firstMinimumFound:
                if value <= firstMinimum:
                    firstMinimum = value
                    firstMinimumPosition = i
                else:
                    firstMinimumFound = True
                    retValue = 0
            else:
                if value > maxValue:
                    maxValue = value
                    maxPosition = i
            i = i + 1
        valid = self.validatePeak(maxPosition)
        if valid:
            self.peaks[indexToFind].maxPosition = maxPosition
            self.peaks[indexToFind].maxValue = maxValue
            self.peaks[indexToFind].valid = True
        return retValue
