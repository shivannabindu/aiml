import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMean of Age Cloumn:",df['Age'].mean())
df=df['Age'].fillna(df['Age'].mean())
print("\nAfter Replacing with Mean:\n\n",df.head(7))
