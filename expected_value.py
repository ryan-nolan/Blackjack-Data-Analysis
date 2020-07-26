#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os
from pathlib import Path
from collections import Counter
import statistics
import sys
import operator

def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct

# %%
#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Data") #insert folder path here
os.chdir(path)
files = os.listdir()
print(sys.argv)

# %%
if len(sys.argv) == 1: 
    for file in files:
        if os.path.isfile(file):
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile)
                print(file)
                chipGainPerHundredHands = {}
                playerStartChipsBeforeHundredHands = 500
                for row in csv_reader:
                    turnNumber = row[0]
                    playerStartChips = row[1]
                    if turnNumber != 'HandNumber':
                        if (int(turnNumber) % 100 == 0):
                            chipGainPerHundredHands[turnNumber] = int(playerStartChips) - playerStartChipsBeforeHundredHands
                            playerStartChipsBeforeHundredHands = int(playerStartChips)
                
                #print(chipGainPerHundredHands)
                print(statistics.mean(chipGainPerHundredHands.values()))
                print(statistics.stdev((chipGainPerHundredHands.values())))
                
                