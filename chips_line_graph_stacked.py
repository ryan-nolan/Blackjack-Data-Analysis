import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os
from pathlib import Path
from collections import Counter
import statistics
import sys

#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
os.chdir(path)
files = os.listdir()

#Auto format for graph
def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct

#x and y bounds for graph, set in args
startChips = 10000
handsPlayed = 25000

#Program must require 2 arguments
if(len(sys.argv) != 3):
    print("This program requires 2 arguments, the starting amount of chips and the amount of hands played")
    exit()
else:
    startChips = int(sys.argv[1])
    handsPlayed = int(sys.argv[2])
    

#Set chart axis and labels
plt.xlim(0, handsPlayed)
plt.ylim(startChips-5000, 25000)
plt.title('Chips Won By Strategy')
plt.xlabel('Hand Number')
plt.ylabel('Chip Count')
plt.gcf().subplots_adjust(left=0.15)

#Parse ever file in data folder
for file in files:
    if os.path.isfile(file):
        with open(file) as csvfile:
            csv_reader = csv.reader(csvfile)
            print(file)
            chips = {}
            #Parse file
            for row in csv_reader:
                turnNumber = row[0]
                chipsValue = row[1]
                chips[turnNumber] = chipsValue
            
            del chips['HandNumber']
            handsShownMod = 10
            listOfChips = []
            for key in chips:
                if(int(key)==0):
                    listOfChips.append(chips[key])
                elif(int(key)==0):
                    listOfChips.append(chips[key])
            valuesAsInt = []
            for val in chips.values():
                valuesAsInt.append(int(val))
                
            StrategyName = file.split('_')[0]
            plt.plot(valuesAsInt)

filenames = []
for file in files:
    if os.path.isfile(file):
        filenames.append(file.split('_')[0]) 

print(filenames)
plt.legend(filenames)
plt.savefig(os.getcwd()+'\\Graphs\\ChipsWonStackedLine\\ChipsWon.png')
