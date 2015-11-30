__author__ = 'jan'
import sys
import getopt
import matplotlib.pyplot as plt
import search.searchinone as run

# from search import datatosearch

__author__ = 'jan'

import spkspectrum
# import matplotlib.pyplot as plt

def readSpectrum(fileName):
    data = []
    try:
        spectrum = spkspectrum.SpkSpectrum(fileName)
        # data = spectrum.read(830)
    except:
        print 'can not read file ' + fileName
    return spectrum

def getFileName():
    fileName = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:s", ["help", "file="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            fileName = a
        else:
            assert False, "unhandled option"
    # ...
    return fileName

def usage():
    print "searchone -fFileName"

def main():
    fileName = getFileName()
    spectrum = readSpectrum(fileName)
    data = spectrum.read(830)
    if len(data) > 0:
        search = run.SearchInOne(data)
        plt.plot(data)
        plt.xlim(0, 1000)
        plt.ylim(0, 10000)

        peaks = search.search()
        moveLineAct = search.getMovingLineAct()
        lineToShow = []
        for item in moveLineAct:
            newItem = 5000 + item*100
            lineToShow.append(newItem)
        plt.plot(lineToShow)

        moveLineVal = search.getMovingLineVal()
        lineToShowVal = []
        for item in moveLineVal:
            newItemV = 4500 + item*100
            lineToShowVal.append(newItemV)
        plt.plot(lineToShowVal)


        lineDist = search.getDistance()
        lineToShowDist = []
        for item in lineDist:
            newItemDist = 1000 + item* 100
            lineToShowDist.append(newItemDist)
        plt.plot(lineToShowDist)

        for peak in peaks:
            plt.scatter(peak[0], peak[1], 30, color='red')

        # plotS = plotSpectrum.PlotSpectrum(data)
        # plotS.analyzeSpectrum(spectrum)
        # # plotSpectrum.PlotSpectrum.analyzeSpectrum(spectrum)
        # plotS.plotSpectrum()
        # # plotSpectrum.PlotSpectrum.plotSpectrum()
        plt.show()

if __name__ == '__main__':
    main()
