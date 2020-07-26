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

def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct

# %%
#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
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
                winPercentage = {}
                for row in csv_reader:
                    turnNumber = row[0]
                    gameResult = row[4]
                    splitGameResult = row[5]

                    winPercentage[turnNumber] = gameResult
                winPercentageCounter = Counter()
                for result in winPercentage.values():
                    winPercentageCounter[result] += 1
                
                sortedWinPercentageFreq = {'W': 0,'L': 0,'D': 0,'W_N': 0, 'L_N' : 0,'D_N': 0}
                for key in winPercentageCounter:
                    if key == 'W':
                        sortedWinPercentageFreq['W'] = winPercentageCounter[key]
                    if key == 'L':
                        sortedWinPercentageFreq['L'] = winPercentageCounter[key]
                    if key == 'D':
                        sortedWinPercentageFreq['D'] = winPercentageCounter[key]
                    if key == 'W_N':
                        sortedWinPercentageFreq['W_N'] = winPercentageCounter[key]
                    if key == 'L_N':
                        sortedWinPercentageFreq['L_N'] = winPercentageCounter[key]
                    if key == 'D_N':
                        sortedWinPercentageFreq['D_N'] = winPercentageCounter[key]
                print(sortedWinPercentageFreq)
                figureObject, axesObject = plt.subplots()
                explode = (0.0, 0.0, 0.0, 0.1, 0.2, 0.3)
                axesObject.pie(sortedWinPercentageFreq.values(), labels=sortedWinPercentageFreq.keys(), autopct=autopct(sortedWinPercentageFreq.values()),startangle=90, explode=explode)

                plt.title(file+ "\nWin Percentage Including Naturals")
                plt.savefig(os.getcwd()+'\\Graphs\\WinPercentagePie\\'+file+'.png')
                #plt.show()
elif len(sys.argv) == 2:
    file = sys.argv[1]
    if os.path.isfile(file):
        with open(file) as csvfile:
            csv_reader = csv.reader(csvfile)
            print(file)
            dealersUpCardFreq = {}
            winPercentage = {}
            chips = {}
            for row in csv_reader:
                turnNumber = row[0]
                gameResult = row[4]
                splitGameResult = row[5]

                winPercentage[turnNumber] = gameResult
            winPercentageCounter = Counter()
            for result in winPercentage.values():
                winPercentageCounter[result] += 1
            
            sortedWinPercentageFreq = {'W': 0,'L': 0,'D': 0,'W_N': 0, 'L_N' : 0,'D_N': 0}
            for key in winPercentageCounter:
                if key == 'W':
                    sortedWinPercentageFreq['W'] = winPercentageCounter[key]
                if key == 'L':
                    sortedWinPercentageFreq['L'] = winPercentageCounter[key]
                if key == 'D':
                    sortedWinPercentageFreq['D'] = winPercentageCounter[key]
                if key == 'W_N':
                    sortedWinPercentageFreq['W_N'] = winPercentageCounter[key]
                if key == 'L_N':
                    sortedWinPercentageFreq['L_N'] = winPercentageCounter[key]
                if key == 'D_N':
                    sortedWinPercentageFreq['D_N'] = winPercentageCounter[key]
            print(sortedWinPercentageFreq)
            figureObject, axesObject = plt.subplots()
            explode = (0.0, 0.0, 0.0, 0.1, 0.2, 0.3)
            axesObject.pie(sortedWinPercentageFreq.values(), labels=sortedWinPercentageFreq.keys(), autopct=autopct(sortedWinPercentageFreq.values()),startangle=90, explode=explode)

            plt.title(file+ "\nWin Percentage Including Naturals")
            plt.savefig(os.getcwd()+'\\Graphs\\WinPercentagePie\\'+file+'.png')
            plt.show()
