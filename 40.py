from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import seaborn as s
df = load_diabetes()
col_n = df.feature_names
df = plt.DataFrame(df.data)
df.columns = col_n
plt.figure(figsize=(8, 10))
s.boxplot(data=df)
plt.title('Multivariate Outliers')
plt.ylabel('Values')
plt.show()   