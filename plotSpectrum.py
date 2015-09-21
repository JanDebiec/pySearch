import sys
from search import datatosearch

__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print sys.argv

    fileName = 'spectra/0016_Schichtdicke,konfokal_14kHz_LAI100.spk'
    # fileName = sys.argv[1]
    # filename os parameter, runs only in pyCharm
    # from console, calleing python plt...py does't work
    spectrum = spkspectrum.SpkSpectrum(fileName)
    data = spectrum.read(830)
    dataToPlot = data[:]

    # moving average size 5, odd can be better to understand, worse to divide
    dataAveraged = spectrum.movingAverage5()
    dataAveragedToPlot = dataAveraged[:]
    # create search class
    searching = datatosearch.DataToSearch(dataAveraged)
    valid0 = searching.level0()
    if valid0 == 0:
        valid1 = searching.level1()
        searching.level2()

    x0 = searching.peaks[0].maxPosition
    y0 = searching.peaks[0].maxValue

    x1 = searching.peaks[1].maxPosition
    y1 = searching.peaks[1].maxValue

    x2 = searching.peaks[2].maxPosition
    y2 = searching.peaks[2].maxValue



    # plot results
    plt.plot(dataToPlot)
    plt.plot(dataAveragedToPlot)
    plt.plot(x0, y0, "r")
    plt.xlabel('spectrum ' + fileName)
    plt.xlim(0, 1000)
    plt.ylim(0, 10000)
    plt.scatter(x0, y0, 30, color='red')
    plt.scatter(x1, y1, 30, color='green')
    plt.scatter(x2, y2, 30, color='blue')
plt.show()