import pandas as p
df=p.read_csv("C:\\ab\\Titanic.csv")
info=df.info()
print("\n\n\nis_na:\n\n",df.isna().head(7))
is_null_su=df.isna().sum()
print("\n\n\nCount of all missing values:\n\n",df.isna().sum())