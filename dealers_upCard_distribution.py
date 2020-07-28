import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os
from pathlib import Path
from collections import Counter
import statistics

#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Source/Data") #insert folder path here
os.chdir(path)
files = os.listdir()

def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct

for file in files:
    if os.path.isfile(file):
        with open(file) as csvfile:
            csv_reader = csv.reader(csvfile)
            print(file)
            dealersUpCardFreq = {}
            for row in csv_reader:
                dealersUpCard = row[15]
                turnNumber = row[0]

                upCardFace = dealersUpCard.split()
                dealersUpCardFreq[turnNumber] = upCardFace[0]
            count = Counter()
            for face in dealersUpCardFreq.values():
                count[face] += 1
            
            sortedDealersUpCardFreq = {'Ace': '0', 'Two': '0', 'Three': '0', 'Four': '0', 'Five': '0', 'Six': '0', 'Seven': '0', 'Eight': '0', 'Nine': '0', 'Ten': '0', 'Jack': '0', 'Queen': '0', 'King': '0'}
            for key in count:
                if key == 'Ace':
                    sortedDealersUpCardFreq['Ace'] = count[key]
                if key == 'Two':
                    sortedDealersUpCardFreq['Two'] = count[key]
                if key == 'Three':
                    sortedDealersUpCardFreq['Three'] = count[key]
                if key == 'Four':
                    sortedDealersUpCardFreq['Four'] = count[key]
                if key == 'Five':
                    sortedDealersUpCardFreq['Five'] = count[key]
                if key == 'Six':
                    sortedDealersUpCardFreq['Six'] = count[key]
                if key == 'Seven':
                    sortedDealersUpCardFreq['Seven'] = count[key]
                if key == 'Eight':
                    sortedDealersUpCardFreq['Eight'] = count[key]
                if key == 'Nine':
                    sortedDealersUpCardFreq['Nine'] = count[key]
                if key == 'Ten':
                    sortedDealersUpCardFreq['Ten'] = count[key]
                if key == 'Jack':
                    sortedDealersUpCardFreq['Jack'] = count[key]
                if key == 'Queen':
                    sortedDealersUpCardFreq['Queen'] = count[key]
                if key == 'King':
                    sortedDealersUpCardFreq['King'] = count[key]

            plt.bar(sortedDealersUpCardFreq.keys(), sortedDealersUpCardFreq.values(), 0.4, color='g')

            mean = statistics.mean(sortedDealersUpCardFreq.values())
            variance = statistics.variance(sortedDealersUpCardFreq.values())
            stdev = statistics.stdev(sortedDealersUpCardFreq.values())

            plt.title(file+ "\nDealer's UpCard Distribution")
            plt.savefig(os.getcwd()+'\\Graphs\\UpCardDistributionHistogram\\'+file+'.png')
            