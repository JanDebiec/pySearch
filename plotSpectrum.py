__author__ = 'jan'
import spkspectrum
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileName = 'spectra/0016_WA-VS_14kHz_LAI100.spk'
    spectrum = spkspectrum.SpkSpectrum(fileName)
    data = spectrum.read(800)
    plt.plot(data)
    plt.ylabel('spectrum ' + fileName)
    plt.show()