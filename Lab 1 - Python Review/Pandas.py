#analyzing, clearing and exploring datasets.
import pandas as pd

#Pandas series (1D labeled array)
a = [1, 7, 2]
series = pd.Series(a)
#print(series)                 # 0, 1, 2 used by default for indexing (labels). series[1] = 7 
series = pd.Series(a, index = ["a", "b", "c"]) 
#print(series)                 #now series["b"] = 7 after we've changed the labels
calories = {"day1": 420, "day2": 380, "day3": 390} #If we turn these into a series, by default the keys becomes the label.
print(pd.Series(calories))                          #Unlike dataframes the dictonary's keys becomes the label.



#dataframes (2D labeled datastructure)
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = table = pd.DataFrame(data)      #can use a custom index.
#print(table)                   #table.loc[0] would return only the first row as a series (column).
#print(table["calories"])       #print the calories column as a series.
#table.loc[7, 'calories'] = 45  #can be used to manually fix outliers.





#mean, median and mode (can be used to fix data):
x = df["Calories"].mean()
x = df["Calories"].median()
x = df["Calories"].mode()[0]                #because the series might have multiple modes.




#if the coleration between is 1 then whenever one is increasing so is the other and vice versa.
df.corr()
#this returns the correlation matrix (has the correlation of each column against the other; thus,  diagonal is 1s)