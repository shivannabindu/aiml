import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print("Before Replacing:\n\n",df['Age'].head(7))
print("\nMode of Age Cloumn:",df['Age'].mode())
df=df['Age'].fillna(df['Age'].median())
print("\nAfter Replacing with Mode:\n\n",df.head(7))
