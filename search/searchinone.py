__author__ = 'jan'

class SearchInOne:
    def __init__(self, data, hillSideLength = 6):
        self.peaks = []
        self.valleys = []
        self.movingAct = []
        self.movingValid = len(data) * [0]
        self.distToSwitchPoint = []
        self.data = data
        self.start = 0
        self.end = len(data)
        self.hillSideLength = hillSideLength

    def getMovingLineAct(self):
        return self.movingAct

    def getMovingLineVal(self):
        return self.movingValid

    def getDistance(self):
        return self.distToSwitchPoint

    def search(self):
        '''
        searching in one step
        :param data:
        :param peakSeparation:
        :return: list of found peaks (pos,  value)
        '''
        i = self.start
        oldValue = self.data[0]
        lastMax = self.data[0]
        lastMaxPos = self.data[0]
        lastMinPos = self.data[0]
        lastMin = self.data[0]
        actSwitchPoint = 0
        lastMovingUp = 0
        actMovingUp = 0
        switchPointCanBeValid = False
        while i < self.end:
            actValue = self.data[i]
            delayed = i - self.hillSideLength
            distFromSwitchPoint = i - actSwitchPoint
            self.distToSwitchPoint.append(distFromSwitchPoint)
            if distFromSwitchPoint > self.hillSideLength:
                switchPointCanBeValid = True
                for x in range(self.hillSideLength):
                    self.movingValid[delayed + x] = self.movingAct[delayed + x]
            if self.movingValid[delayed] > 0:
                if self.data[delayed] > lastMax:
                    lastMax = self.data[delayed]
                    lastMaxPos = delayed
            elif self.movingValid[delayed] < 0:
                if self.data[delayed] < lastMin:
                    lastMin = self.data[delayed]
                    lastMinPos = delayed
            # moving up
            if actValue > oldValue:
                actMovingUp = 1
            # moving down
            elif actValue < oldValue:
                actMovingUp =  -1
            else:
                actMovingUp = 0

            oldValue = actValue
            self.movingAct.append(actMovingUp)
            if actMovingUp != lastMovingUp:
                if switchPointCanBeValid:
                    switchPointCanBeValid = False
                    if lastMovingUp > 0:
                        point = (i-1, self.data[i-1])
                        self.peaks.append(point)
                actSwitchPoint = i
            lastMovingUp = actMovingUp
            i = i + 1
        return self.peaks