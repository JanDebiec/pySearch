__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileName = 'spectra/0016_Schichtdicke,konfokal_14kHz_LAI100.spk'
    spectrum = spkspectrum.SpkSpectrum(fileName)
    data = spectrum.read(830)
    dataToPlot = data[16:]
    plt.plot(dataToPlot)
    plt.xlabel('spectrum ' + fileName)
    plt.show()