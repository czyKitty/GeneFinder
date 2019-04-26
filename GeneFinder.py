import sys
import random
from load import *
from dna import *

def oneFrame(DNA):
    orf_List = []
    i = 0
    stopCodon = ["TAG","TGA","TAA"]
    while i < len(DNA):
        if DNA[i:i+3] == "ATG":
            j = i
            while DNA[j:j+3] not in stopCodon and j < len(DNA):
                j += 3
            if DNA[i:j] != "ATG":
                orf_List.append(DNA[i:j])
        i += 3
    return orf_List

def oneFrameV2(DNA):
    orf_List = oneFrame(DNA)
    new_orf_list = []
    for i in range(len(orf_List)-1):
        new_orf_list.append(orf_List[i])
        if orf_List[i+1] in orf_List[i]:
            i += 2
        else:
            i += 1
    return new_orf_list

def longestORF(DNA):
    maxORF = ""
    for i in range(3):
        list = oneFrameV2(DNA[i:])
        if len(list) != 0 and len(maxORF)<len(max(list,key=len)):
            maxORF = max(list,key=len)
    return maxORF


def longestORFBothStrands(DNA):
    list = []
    list.append(longestORF(DNA))
    list.append(longestORF(reverseComplement(DNA)))
    if len(list) != 0:
        return max(list,key=len)
    else:
        return ""

def collapse(list):
    return "".join(list)

def longestORFNoncoding(DNA, numReps):
    dnaList = list(DNA)
    maxLen = 0
    for i in range(numReps):
        random.shuffle(dnaList)
        garbSeq = longestORFBothStrands(collapse(dnaList))
        if maxLen < len(garbSeq):
            maxLen = len(garbSeq)
    return maxLen

def findORFs(DNA):
    maxORF = []
    for i in range(3):
        list = oneFrameV2(DNA[i:])
        if len(list) != 0:
            maxORF.append(max(list,key=len))
    return maxORF

def findORFsBothStrands(DNA):
    return findORFs(DNA)+findORFs(reverseComplement(DNA))

def getCoordinates(orf,DNA):
    list = []
    start = DNA.find(orf)
    if start != -1:
        list.append(start)
        list.append(start+len(orf))
        return list
    else:
        start = reverseComplement(DNA).find(orf)
        list.append(start)
        list.append(start+len(orf))
        return list

def geneFinder(DNA, minLen):
    finalOutputList = []
    ORFList = findORFsBothStrands(DNA)
    for item in ORFList:
        if len(item) >= minLen:
            tempList = getCoordinates(item,DNA)
            tempList.append(codingStrandToAA(item))
            finalOutputList.append(tempList)
    finalOutputList.sort()
    return finalOutputList

def printGenes(geneList):
    for item in geneList:
        print(item)


def main():
    DNA = loadSeq("X73525.fa")
    minLen = longestORFNoncoding(DNA,1500)
    printGenes(geneFinder(DNA,minLen))
main()