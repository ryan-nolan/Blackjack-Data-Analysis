#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import csv
import os
from pathlib import Path
from collections import Counter
import statistics


# %%
#File Handling
path = Path("C:/Users/Ryan/Desktop/Dissertation/Data") #insert folder path here
os.chdir(path)
files = os.listdir()

def autopct(values):
    def my_autopct(pct):
        sumOf = sum(values)
        ret = int(round(pct * sumOf / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=ret)
    return my_autopct
# %%
for file in files:
    if os.path.isfile(file):
        with open(file) as csvfile:
            csv_reader = csv.reader(csvfile)
            print(file)
            chips = {}
            for row in csv_reader:
                turnNumber = row[0]
                chipsValue = row[1]
                chips[turnNumber] = chipsValue
            
            del chips['HandNumber']
            #print(chips)
            handsShownMod = 10
            listOfChips = []
            for key in chips:
                if(int(key)==0):
                    listOfChips.append(chips[key])
                elif(int(key)==0):
                    listOfChips.append(chips[key])
            #print(listOfChips)
            
            x1 = (int(list(chips)[-1]))
            x0 = int(list(chips)[0])
            valuesAsInt = []
            for val in chips.values():
                valuesAsInt.append(int(val))
            y1 = max(valuesAsInt)
            y0 = min(valuesAsInt)
            #print(valuesAsInt)
            plt.plot(valuesAsInt)
            plt.xlim(x0, x1)
            plt.ylim(y0-100, y1+100)
            plt.title(file + '\nChip Count Per Turn')
            plt.savefig(os.getcwd()+'\\Graphs\\ChipsWonLine\\'+file+'.png')
            
            plt.show()
        


# %%
