import pandas as pd
df=pd.read_csv("C:\\ab\\Titanic.csv")
print("\nBefore Droping:\n")
df.info()
df=df.dropna(axis=1)
print('\n\nAfter Droping:\n')
df.info()
