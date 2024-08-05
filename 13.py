import pandas as pd 
from matplotlib import pyplot as plt 
t = pd.read_csv("C:\\ab\\Iris1.csv") 
 
Species_colors = {'Iris-setosa': 'k','Iris-versicolor': 'g','Iris-virginica': 'r'} 
for Species, color in Species_colors.items(): 
    sl = t[t['Species'] == Species]['sepal_length'] 
    sw = t[t['Species'] == Species]['sepal_width'] 
    plt.scatter(sl, sw, color=color, label=Species) 
 
plt.legend() 
plt.xlabel('sepal_length') 
plt.ylabel('sepal_width') 
plt.title('sepal Width and Length for Iris Species') 
plt.show()