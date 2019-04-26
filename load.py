import math
import random
import sys
import string

def loadSeq(fileName):
    dnaFile = open(fileName,'r')
    dna = ""
    for line in dnaFile:
        if line[0] != ">":
            dna += line.replace("\n","")
    dnaFile.close()
    return dna