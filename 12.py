import pandas as pd 
import matplotlib.pyplot as plt 
data={'temp':[22,25,28,30,32,35,38,40,42,45]} 
index=pd.date_range(start='2023-07-01',periods=len(data))
df=pd.DataFrame(data)
df.plot(color='k',linewidth=1)
plt.xticks(rotation=25)
plt.ylabel('temp')
plt.xlabel('date')
plt.show()