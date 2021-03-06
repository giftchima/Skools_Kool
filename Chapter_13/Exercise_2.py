__author__ = 'matt'
"""
Go to Project Gutenberg (gutenberg.org) and download your favorite out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times each word is used.

Print the number of different words used in the book. Compare different books by different authors, written in different eras. Which author uses the most extensive vocabulary?
"""

import sys, string
from collections import OrderedDict

def processLine(sin, din):
    """For a given line, append to a dictionary individual words and counts"""
    line = sin.strip()
    words = line.split()
    for word in words:
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        word = word.translate(string.maketrans("",""), string.punctuation + string.digits)
        word = word.lower()
        # Works, but could be made shorter
#        if word in din:
#            din[word] += 1
#        else:
#            din[word] = 1
        # Use get method to check for key. If key is not present, use value of 0.
        # Reassign new key value
        din[word] = 1 + din.get(word, 0)
    return din


def processFile(fin, processFunc):
    """Return an ordered dictionary of distinct words and occurance counts, along with total word count"""
    d = dict()
    try:
        myFile = open(fin, 'r')
        for line in myFile.readlines():
            processFunc(line, d)
        distinctWords = len(d) # Get a distinct word count.
        # Create an OrderedDictionary. Use t[0] to sort by key, use t[1] to sort by value.
        sortedDict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
        return sortedDict, distinctWords
    except:
        e = sys.exc_info()
        print e
    finally:
        myFile.close()

if __name__ == '__main__':
    bookFile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/Books/moby_dick.txt'
    infile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/testtext.txt'
    words, distinctWordCount = processFile(bookFile, processLine)
    print words
    print distinctWordCount

