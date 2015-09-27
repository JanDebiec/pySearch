__author__ = 'jan'
import sys
import getopt
import plotSpectrum

# from search import datatosearch

__author__ = 'jan'

import spkspectrum
# import matplotlib.pyplot as plt

def readSpectrum(fileName):
    data = []
    try:
        spectrum = spkspectrum.SpkSpectrum(fileName)
        data = spectrum.read(830)
    except:
        print 'can not read file ' + fileName
    return data

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
    print "analyzeSpectrum -fFileName"

def main():
    fileName = getFileName()
    data = readSpectrum(fileName)
    if len(data)> 0:
        plotSpectrum.analyzeSpectrum(data)
        plotSpectrum.plotSpectrum()

if __name__ == '__main__':
    main()
