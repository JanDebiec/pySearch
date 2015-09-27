#import sys
# import getopt

from search import datatosearch

__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

# if __name__ == '__main__':
#     print sys.argv

    # fileName = 'spectra/0016_Schichtdicke,konfokal_14kHz_LAI100.spk'
    # # fileName = sys.argv[1]
    # # filename os parameter, runs only in pyCharm
    # # from console, calleing python plt...py does't work
    # spectrum = spkspectrum.SpkSpectrum(fileName)
    # data = spectrum.read(830)


def analyzeSpectrum(data):
    dataToPlot = data[:]

    # moving average size 5, odd can be better to understand, worse to divide
    dataAveraged = spectrum.movingAverage5()
    dataAveragedToPlot = dataAveraged[:]
    # create search class
    searching = datatosearch.DataToSearch(dataAveraged)
    valid0 = searching.level0()
    if valid0 == 0:
        [valid11, valid12] = searching.level1()
        [valid21, valid22, valid23, valid24] = searching.level2()

def plotSpectrum():
    x0 = searching.peaks[0].maxPosition
    y0 = searching.peaks[0].maxValue

    # plot results
    plt.plot(dataToPlot)
    plt.plot(dataAveragedToPlot)
    plt.xlabel('spectrum ' + fileName)
    plt.xlim(0, 1000)
    plt.ylim(0, 10000)

    # peak 0
    # plt.plot(x0, y0, "r")
    plt.scatter(x0, y0, 30, color='red')
    if valid11 == 0:
        x0minL = searching.peaks[0].leftBorder
        y0minL = searching.peaks[0].leftBorderValue
        plt.scatter(x0minL, y0minL, 40, color='red')
        if searching.peaks[1].valid == True:
            x1 = searching.peaks[1].maxPosition
            y1 = searching.peaks[1].maxValue
            plt.scatter(x1, y1, 30, color='blue')
        if valid21 == 0:
            x1minL = searching.peaks[1].leftBorder
            y1minL = searching.peaks[1].leftBorderValue
            plt.scatter(x1minL, y1minL, 40, color='blue')
        if valid22 == 0:
            x1minR = searching.peaks[1].rightBorder
            y1minR = searching.peaks[1].rightBorderValue
            plt.scatter(x1minR, y1minR, 40, color='blue')

    if valid12 == 0:
        x0minR = searching.peaks[0].rightBorder
        y0minR = searching.peaks[0].rightBorderValue
        plt.scatter(x0minR, y0minR, 40, color='red')
        if searching.peaks[2].valid == True:
            x2 = searching.peaks[2].maxPosition
            y2 = searching.peaks[2].maxValue
            plt.scatter(x2, y2, 30, color='green')
        if valid23 == 0:
            x2minL = searching.peaks[2].leftBorder
            y2minL = searching.peaks[2].leftBorderValue
            plt.scatter(x2minL, y2minL, 40, color='blue')
        if valid24 == 0:
            x2minR = searching.peaks[2].rightBorder
            y2minR = searching.peaks[2].rightBorderValue
            plt.scatter(x2minR, y2minR, 40, color='blue')

    plt.show()