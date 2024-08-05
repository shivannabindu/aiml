import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print("Before Filling Null values:\n\n",df.isna().sum())
df=df.fillna(0)
print("\n\nAfter Filling Null values:\n\n",df.isna().sum())