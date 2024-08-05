import pandas as pd 
a = pd.Series([10, 20, 30, 40, 50]) 
b = pd.Series([40, 50, 60, 70, 80]) 
print("Series A:") 
print(a) 
print("\nSeries B:") 
print(b) 
 
non_com = a[~a.isin(b)].tolist() + b[~b.isin(a)].tolist() 
print("Items not common to both Series:") 
print(non_com) 
 
print("\nSmallest element in Series A:\n", a.min()) 
print("\nLargest element in Series A:\n",a.max()) 
 
print("\nSum of Series B:\n", b.sum()) 
print("\nAverage of Series A:\n",a.mean()) 
print("\nMedian of Series B:\n", a.median())