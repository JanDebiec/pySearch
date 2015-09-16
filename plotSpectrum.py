__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileName = 'spectra/0016_Schichtdicke,konfokal_14kHz_LAI100.spk'
    spectrum = spkspectrum.SpkSpectrum(fileName)
    data = spectrum.read(830)
    dataToPlot = data
    # dataToPlot = data[16:]
    dataAveraged = spectrum.movingAverage5()
    plt.plot(dataToPlot)
    plt.plot(dataAveraged)
    plt.xlabel('spectrum ' + fileName)
    plt.show()