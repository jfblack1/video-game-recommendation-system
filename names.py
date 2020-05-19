'''
Created on Mar 2, 2020

@author: jfbla
'''
#This script prints out the names of each video game in the "Video_Games" csv file
#with HTML option tags surrounding each name. The output file is called "names.txt".
import pandas as pd
from pathlib import Path

df=pd.read_csv('Video_Games.csv', header=None)
df=df.drop ([0])


f = open ("names.txt", mode='x')
rows=df.iterrows()
for row in rows:
    s = "<option>" + row[1][0] + "</option>"
    print (s, file=f)
