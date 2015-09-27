#import sys
# import getopt

from search import datatosearch

__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

class PlotSpectrum:
    def __init__(self, data):
        self.searching = None
        self.valid0 = -1
        self.valid1 = []
        self.valid2 = []
        self.searching = None
        self.dataAveraged = []
        self.dataAveragedToPlot = []
        self.data = data

    def analyzeSpectrum(self, spectrum):
        # self.data = spectrum.read(830)
        # dataToPlot = data[:]

        # moving average size 5, odd can be better to understand, worse to divide
        self.dataAveraged = spectrum.movingAverage5()
        self.dataAveragedToPlot = self.dataAveraged[:]
        # create search class
        self.searching = datatosearch.DataToSearch(self.dataAveraged)
        valid0 = self.searching.level0()
        if valid0 == 0:
            self.valid1 = self.searching.level1()
            # [valid11, valid12] = searching.level1()
            self.valid2 = self.searching.level2()
            # [valid21, valid22, valid23, valid24] = searching.level2()

    def plotSpectrum(self):
        x0 = self.searching.peaks[0].maxPosition
        y0 = self.searching.peaks[0].maxValue

        # plot results
        # plt.plot(dataToPlot)
        plt.plot(self.dataAveragedToPlot)
        # plt.xlabel('spectrum ' + fileName)
        plt.xlim(0, 1000)
        plt.ylim(0, 10000)

        # peak 0
        # plt.plot(x0, y0, "r")
        plt.scatter(x0, y0, 30, color='red')
        if self.valid1[0] == 0:
            x0minL = self.searching.peaks[0].leftBorder
            y0minL = self.searching.peaks[0].leftBorderValue
            plt.scatter(x0minL, y0minL, 40, color='red')
            if self.searching.peaks[1].valid == True:
                x1 = self.searching.peaks[1].maxPosition
                y1 = self.searching.peaks[1].maxValue
                plt.scatter(x1, y1, 30, color='blue')
            if self.valid2[0] == 0:
                x1minL = self.searching.peaks[1].leftBorder
                y1minL = self.searching.peaks[1].leftBorderValue
                plt.scatter(x1minL, y1minL, 40, color='blue')
            if self.valid2[1] == 0:
                x1minR = self.searching.peaks[1].rightBorder
                y1minR = self.searching.peaks[1].rightBorderValue
                plt.scatter(x1minR, y1minR, 40, color='blue')

        if self.valid1[1] == 0:
            x0minR = self.searching.peaks[0].rightBorder
            y0minR = self.searching.peaks[0].rightBorderValue
            plt.scatter(x0minR, y0minR, 40, color='red')
            if self.searching.peaks[2].valid == True:
                x2 = self.searching.peaks[2].maxPosition
                y2 = self.searching.peaks[2].maxValue
                plt.scatter(x2, y2, 30, color='green')
            if self.valid2[2] == 0:
                x2minL = self.searching.peaks[2].leftBorder
                y2minL = self.searching.peaks[2].leftBorderValue
                plt.scatter(x2minL, y2minL, 40, color='blue')
            if self.valid2[3] == 0:
                x2minR = self.searching.peaks[2].rightBorder
                y2minR = self.searching.peaks[2].rightBorderValue
                plt.scatter(x2minR, y2minR, 40, color='blue')

        plt.show()