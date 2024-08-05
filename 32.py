import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print(df.isna().sum())
df=df.replace({pd.nan:-1})
print("\n\n\n")
print(df.isna().sum())