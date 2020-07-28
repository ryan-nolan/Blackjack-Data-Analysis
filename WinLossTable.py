""" Strategy Name	StartingChips	End Chips	Chips Won	Action (Total Sum of stakes)	Win%	Loss%	Tie %	W/L Ratio	
    Strat 1	d	d	d	d	d	d	d	d	
    Strat 2									
    Strat 3									
    Strat 4									
			                                                                                                                     Table 2 layout"""

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

#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
os.chdir(path)
files = os.listdir()
print(sys.argv)

startChips = 10000
turnsPlayed = 25000

#Program must require 2 arguments
if(len(sys.argv) != 3):
    print("This program requires 2 arguments, the starting amount of chips and the amount of hands played")
    exit()
else:
    startChips = int(sys.argv[1])
    turnsPlayed = int(sys.argv[2])
    

#Create table
os.chdir('Graphs')
with open('WinLossTable.csv', 'w', newline='') as csv_output_file:
    writer = csv.writer(csv_output_file)
    writer.writerow(['Strategy Name', 'Starting Chips', 'End Chips', 'Chips Won', 'Action', 'Win%','Loss%','Tie%','Win/Loss%'])
    os.chdir('..')

    for file in files:
        if os.path.isfile(file):
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile)
                print(file)

                winlossPercentage = {}
                action = 0
                stakesWon = 0
                for row in csv_reader:
                    turnNumber = row[0]
                    gameResult = row[4]
                    splitGameResult = row[5]
                    endChips = row[2]
                    if turnNumber != 'HandNumber':
                        action += int(row[8])
                    if turnNumber != 'HandNumber':
                        stakesWon += int(row[3])
                    winlossPercentage[turnNumber] = gameResult


                winPercentageCounter = Counter()
                for result in winlossPercentage.values():
                    winPercentageCounter[result] += 1
                #Tabulate win percentage
                sortedWinPercentageFreq = {'W': 0,'L': 0,'D': 0}
                for key in winPercentageCounter:
                    if key == 'W':
                        sortedWinPercentageFreq['W'] = winPercentageCounter[key]
                    if key == 'L':
                        sortedWinPercentageFreq['L'] = winPercentageCounter[key]
                    if key == 'D':
                        sortedWinPercentageFreq['D'] = winPercentageCounter[key]
                    if key == 'W_N':
                        sortedWinPercentageFreq['W'] += winPercentageCounter[key]
                    if key == 'L_N':
                        sortedWinPercentageFreq['L'] += winPercentageCounter[key]
                    if key == 'D_N':
                        sortedWinPercentageFreq['D'] += winPercentageCounter[key]

                #Calculate Win Ratios
                winPercentage = (sortedWinPercentageFreq['W'] / (sortedWinPercentageFreq['W']+sortedWinPercentageFreq['L']+sortedWinPercentageFreq['D']))*100
                lossPercentage = (sortedWinPercentageFreq['L'] / (sortedWinPercentageFreq['W']+sortedWinPercentageFreq['L']+sortedWinPercentageFreq['D']))*100
                drawPercentage = (sortedWinPercentageFreq['D'] / (sortedWinPercentageFreq['W']+sortedWinPercentageFreq['L']+sortedWinPercentageFreq['D']))*100
                print("Win%:\t"+str(winPercentage))
                print("Loss%:\t"+str(lossPercentage))
                print("Draw%:\t"+str(drawPercentage))
                winLossRatio = (winPercentage / (winPercentage+lossPercentage)) * 100
                print("Win/Loss%:\t"+str(winLossRatio))
                
                print("Start Chips:\t"+str(startChips))
                print("End Chips:\t"+str(endChips))
                chipsWon = int(endChips) - startChips
                print("Chips Won:\t"+str(chipsWon))
                print("Action%:\t"+str(action))
                print("Stakes won:\t"+str(stakesWon))
                StrategyName = file.split('_')[0]

                
                writer.writerow([StrategyName, str(startChips), str(endChips), str(chipsWon), str(action), '{:.3f}'.format(winPercentage),
                '{:.3f}'.format(lossPercentage),'{:.3f}'.format(drawPercentage),'{:.3f}'.format(winLossRatio)])

                            
