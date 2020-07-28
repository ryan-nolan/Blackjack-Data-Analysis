""" Strategy Name	NonMinBet%	ChipsWonWhenMinBet	Chips Won when not minBet	100 hand mean	100 hand std dev
    Strat 1					
    Strat 2					
    Strat 3					
    Strat 4					                                                                                            Table 2 layout"""

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

if(len(sys.argv) != 3):
    print("This program requires 2 arguments, the starting amount of chips and the minimum bets")
    exit()
else:
    playerStartChipsBeforeHundredHands = int(sys.argv[1])
    minBet = int(sys.argv[2])

os.chdir('Graphs')
#Open table file
with open('ExpectedValueTable.csv', 'w', newline='') as csv_output_file:
    writer = csv.writer(csv_output_file)
    writer.writerow(['Strategy Name', 'NonMinBet%', 'Chips Won When Min Betting', 'Chips Won When Non Min Betting', 'Expected Value (100 hands)', 'Std Deviation'])
    os.chdir('..')
    for file in files:
        if os.path.isfile(file):
            with open(file) as csvfile:
                csv_reader = csv.reader(csvfile)
                print(file)
                chipGainPerHundredHands = {}
                overMinBetPercentage = {}
                chipsWonWhenStake = {}
                #Parse file
                for row in csv_reader:
                    turnNumber = row[0]
                    playerStartChips = row[1]
                    stake = row[8]
                    chipsWon = row[3]
                    overMinBetPercentage[turnNumber] = stake
                    chipsWonWhenStake[turnNumber] = (stake, chipsWon)
                    if turnNumber != 'HandNumber':
                        if (int(turnNumber) % 100 == 0):
                            chipGainPerHundredHands[turnNumber] = int(playerStartChips) - playerStartChipsBeforeHundredHands
                            playerStartChipsBeforeHundredHands = int(playerStartChips)
                
                overMinBetCounter = Counter()
                for result in overMinBetPercentage.values():
                    overMinBetCounter[result] += 1
                del overMinBetCounter['PlayerStake']

                #Calculate NonMinBet%
                sortedOverMinBetFreq = {'MinBet' : 0, 'Above MinBet': 0}
                for key in overMinBetCounter:
                    
                    if key == str(minBet):
                        sortedOverMinBetFreq['MinBet'] += overMinBetCounter[key]
                    else:
                        sortedOverMinBetFreq['Above MinBet'] += overMinBetCounter[key]
                NotMinBetPercentage = (sortedOverMinBetFreq['Above MinBet'] / (sortedOverMinBetFreq['Above MinBet'] + sortedOverMinBetFreq['MinBet']))*100

                #Calculate Chips won when NonMinBet
                del chipsWonWhenStake['HandNumber']
                ChipsWonWhenMinBet = 0
                ChipsWonWhenNotMinBet = 0
                for key in chipsWonWhenStake:
                    if int(chipsWonWhenStake[key][0]) == minBet:
                        ChipsWonWhenMinBet += int(chipsWonWhenStake[key][1])
                    else :
                        ChipsWonWhenNotMinBet += int(chipsWonWhenStake[key][1])
                StrategyName = file.split('_')[0]
                print(StrategyName)   
                #Calculate Expected Value and Std Deviation 
                ev = statistics.mean(chipGainPerHundredHands.values())
                stddev = statistics.stdev((chipGainPerHundredHands.values()))
                #Write to file
                writer.writerow([StrategyName, '{:.3f}'.format(NotMinBetPercentage)+'%', ChipsWonWhenMinBet, ChipsWonWhenNotMinBet, '{:f}'.format(ev), '{:f}'.format(stddev)])

                        
