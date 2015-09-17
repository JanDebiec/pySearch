# from search import datatosearch
from search import datatosearch
# from search.datatosearch import *

__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileName = 'spectra/0016_Schichtdicke,konfokal_14kHz_LAI100.spk'
    spectrum = spkspectrum.SpkSpectrum(fileName)
    data = spectrum.read(830)
    dataToPlot = data

    # moving average size 5, odd can be better to understand, worse to divide
    dataAveraged = spectrum.movingAverage5()

    # create search class
    searching = datatosearch.DataToSearch(dataAveraged)
    valid = searching.level0()

    x0 = searching.peaks[0].maxPosition
    y0 = searching.peaks[0].maxValue

    # plot results
    plt.plot(dataToPlot)
    plt.plot(dataAveraged)
    plt.plot(x0, y0, "r")
    plt.xlabel('spectrum ' + fileName)
    plt.show()