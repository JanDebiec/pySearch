# from search import spectrumpeak
from spectrumpeak import SpectrumPeak

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
        self.valid0 = -1
        self.valid11 = -1
        self.valid12 = -1
        self.valid21 = -1
        self.valid22 = -1
        self.valid23 = -1
        self.valid24 = -1
        self.indexToSecondPeak = -1

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
        return self.valid0

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
        self.valid11 = self.searchToLeft(1, 0)
        if(self.valid11 != 0):
            self.peaks[0].leftBorder = self.start
            self.peaks[0].leftBorderValue = self.data[self.start]

        # search from peak0 to right, to end
        self.actStart = self.peaks[0].maxPosition
        self.actEnd = self.end
        self.valid12 = self.searchToRight(2, 0)
        if(self.valid12 != 0):
            self.peaks[0].rightBorder = self.end
            self.peaks[0].rightBorderValue = self.data[self.end]


        return [self.valid11,  self.valid12]

    def level2(self):
        '''

        :return:
        '''
        if self.valid11 == 0:
            # search from peak 1 to left
            self.actStart = self.peaks[1].maxPosition
            self.actEnd = self.start
            self.valid21 = self.searchToLeft(3, 1)

            # search from peak 1 to right, to peak 0
            self.actStart = self.peaks[1].maxPosition
            self.actEnd = self.peaks[0].leftBorder
            self.valid22 = self.searchToRight(4, 1)

        if self.valid12 == 0:
            # search from peak 2 to left, to peak 0
            self.actStart = self.peaks[2].maxPosition
            self.actEnd = self.peaks[0].rightBorder
            self.valid23 = self.searchToLeft(5, 2)

            # search fr0m peak 2 to right, to end
            self.actStart = self.peaks[2].maxPosition
            self.actEnd = self.end
            self.valid24 = self.searchToRight(6, 2)

        # validate peaks 1 and 2
        # find higher from both
        if self.peaks[1].maxValue >= self.peaks[2].maxValue:
            self.indexToSecondPeak = 1
        else:
            self.indexToSecondPeak = 2

        return [self.valid21, self.valid22, self.valid23, self.valid24]

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
        if firstMinimumFound:
            self.peaks[indexToUpdate].leftBorder = firstMinimumPosition
            self.peaks[indexToUpdate].leftBorderValue = firstMinimum
            retValue = 0
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
        if firstMinimumFound:
            self.peaks[indexToUpdate].rightBorder = firstMinimumPosition
            self.peaks[indexToUpdate].rightBorderValue = firstMinimum
            retValue = 0
        return retValue
