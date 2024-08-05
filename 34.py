import pandas as p
df=p.read_csv("C:\\ab\\Titanic.csv")
print('\n\Before Droping:\n')
df.info()
df=df.dropna()
print('\n\nAfter Droping:\n')
df.info()