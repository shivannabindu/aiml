import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(78))
print("\nMedian of Age Cloumn:",df['Age'].median())
df=df['Age'].fillna(df['Age'].median())
print("\nAfter Replacing with Mean:\n\n",df.head(90))
