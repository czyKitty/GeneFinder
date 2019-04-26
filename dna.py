import math
import random
import sys
import string

def reverseComplement(DNA):
    complement = ""
    for i in range(len(DNA)):
        base = DNA[len(DNA)-i-1]
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
    return complement

def codingStrandToAA(DNA):
    if len(DNA)/3 != len(DNA)/3:
        print("DNA sequence is not divisible by 3.")
        return None
    else:
        protein = ""
        for i in range(len(DNA)//3):
            sequence = DNA[3*i:3*i+3]
            if sequence == "TTT" or sequence == "TTC":
                protein += "F"
            elif sequence == "TTA" or sequence == "TTG" or sequence == "CTT"or sequence == "CTC" or sequence == "CTA" or sequence == "CTG":
                protein += "L"
            elif sequence == "ATT" or sequence == "ATC" or sequence == "ATA":
                protein += "I"
            elif sequence == "ATG":
                protein += "M"
            elif sequence == "GTT" or sequence == "GTC" or sequence == "GTA" or sequence == "GTG":
                protein += "V"
            elif sequence == "TCT" or sequence == "TCC" or sequence == "TCA" or sequence == "TCG":
                protein += "S"
            elif sequence == "CCT" or sequence == "CCC" or sequence == "CCA" or sequence == "CCG":
                protein += "P"
            elif sequence == "ACT" or sequence == "ACC" or sequence == "ACA" or sequence == "ACG":
                protein += "T"
            elif sequence == "GCT" or sequence == "GCC" or sequence == "GCA" or sequence == "GCG":
                protein += "A"
            elif sequence == "TAT" or sequence == "TAC":
                protein += "Y"
            elif sequence == "CAT" or sequence == "CAC":
                protein += "H"
            elif sequence == "CAA" or sequence == "CAG":
                protein += "Q"
            elif sequence == "AAT" or sequence == "AAC":
                protein += "N"
            elif sequence == "TAT" or sequence == "TAC":
                protein += "Y"
            elif sequence == "AAA" or sequence == "AAG":
                protein += "K"
            elif sequence == "GAT" or sequence == "GAC":
                protein += "D"
            elif sequence == "GAA" or sequence == "GAG":
                protein += "E"
            elif sequence == "TGT" or sequence == "TGC":
                protein += "C"
            elif sequence == "TGG":
                protein += "W"
            elif sequence == "CGT" or sequence == "CGC" or sequence == "CGA"or sequence == "CGG" or sequence == "AGA" or sequence == "AGG":
                protein += "R"
            elif sequence == "AGT" or sequence == "AGC":
                protein += "S"
            elif sequence == "GGT"or"GGC"or"GGA"or"GGG":
                protein += "G"
        return protein