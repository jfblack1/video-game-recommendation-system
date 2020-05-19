#This script prints out the rows in "Video_Games.csv" with JavaScript array characters.
#The output is an array of arrays. each row is an array. Each column in each row is 
#a different element in that row, separated by commas.
import pandas as pd

df=pd.read_csv('./Video_Games.csv', header=None)
headers=['Name','Genre','Year_Of_Release','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales','Critic_Score','Critic_Count','User_Score','User_Count']
df.columns=headers
df.drop(index=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df[['Name','Genre']]=df[['Name','Genre']].astype("str")
df[['Year_Of_Release']]=df[['Year_Of_Release']].astype("float")
df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','User_Score','Global_Sales']]=df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales','User_Score','Global_Sales']].astype("float")
df[['Critic_Score','Critic_Count','User_Count']]=df[['Critic_Score','Critic_Count','User_Count']].astype("float")
rows=df.iterrows();

f = open ("rows.txt", mode='x')
for row in rows:
    s = "[" + "\"" + row[1]['Name'] + "\"" + "," + "\"" + row[1]['Genre'] + "\"" + "," + str(row[1]['Global_Sales']) + "," + str(row[1]['Critic_Score']) + "," + str(row[1]['User_Score']) + "],"
    print (s, file=f)
    