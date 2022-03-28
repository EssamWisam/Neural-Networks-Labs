import pandas as pd
df = pd.read_csv('data.csv')    #becomes a dataframe.
#printing info about the data
#print(df.info())
#among other things, it states the no. of entries that have NaN(missing) in some column for each.
#we usually want to clean up the data from those rows, we can do this by:
df.dropna(inplace = True)
df.fillna(130, inplace = True)              #In case we prefer to rather replace the NaNs 
df["Calories"].fillna(130, inplace = True)  #In case we'd like to do so only for a specific column


#manually fix outliers:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120 
    #or do:     df.drop(x, inplace = True)





#In case one of the columns has wrong data. If it can't be saved it will be converted to NaT (not a time)
df['Date'] = pd.to_datetime(df['Date'])



#Duplicates:
print(df.duplicated())      #gives you a series, each entry is a boolean. If it's true then that row is duplicated.
df.drop_duplicates(inplace = True)