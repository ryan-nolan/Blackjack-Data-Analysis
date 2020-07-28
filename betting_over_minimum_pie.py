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

#Auto Format graphs
def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct


#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
os.chdir(path)
files = os.listdir()
print(sys.argv)

#If no args
if len(sys.argv) == 1: 
    for file in files:
        if os.path.isfile(file):
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile)
                print(file)
                overMinBetPercentage = {}
                #Parse file
                for row in csv_reader:
                    turnNumber = row[0]
                    stake = row[8]
                    overMinBetPercentage[turnNumber] = stake
                #Count MinBets and NonMinBets
                overMinBetCounter = Counter()
                for result in overMinBetPercentage.values():
                    overMinBetCounter[result] += 1
                del overMinBetCounter['PlayerStake']

                minBetString = overMinBetCounter.most_common(1)[0][0]
                #Sort dictionary
                sortedOverMinBetFreq = {'MinBet' : 0, 'Above MinBet': 0}
                for key in overMinBetCounter:
                    if key == minBetString:
                        sortedOverMinBetFreq['MinBet'] += overMinBetCounter[key]
                    else:
                        sortedOverMinBetFreq['Above MinBet'] += overMinBetCounter[key]

                #Plot pie chart
                figureObject, axesObject = plt.subplots()
                axesObject.pie(sortedOverMinBetFreq.values(), labels=sortedOverMinBetFreq.keys(), autopct=autopct(sortedOverMinBetFreq.values()),startangle=90)

                plt.title(file+ "\nMinimum Bet Percentage")
                plt.savefig(os.getcwd()+'\\Graphs\\AboveMinBetPie\\'+file+'.png')
