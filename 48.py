import pandas as p 
da=p.read_csv("C:\\ab\\Dhoni_International_wk_data.csv") 
da.info() 
 
#PRE_PROCESSING 
miss=da.isna().sum() 
print("\nMissing Values:\n",miss) 
da.dropna(inplace=True) 
print("\nMissing Values:\n",da.isna().sum()) 
import matplotlib.pyplot as m 
import seaborn as s 
m.figure(figsize=(18,10)) 
s.histplot(da['Catches'], bins=15, kde=True) 
m.title('Distribution of Catches') 
m.show() 
m.figure(figsize=(18,10)) 
s.barplot(data=da,x='Catches_as_wk',y='Catches',palette='viridis') 
m.title('Batting Scores Over the Catches') 
m.xlabel('Ground');m.ylabel('Catches') 
m.xticks(rotation=45);m.show() 
m.figure(figsize=(18,10)) 
s.heatmap(data=da.corr(),annot=True,cmap='crest') 
m.title("Heatmap on DHONI's stats") 
m.show() 
import matplotlib.pyplot as m 
import seaborn as s 
m.figure(figsize=(18,10)) 
s.histplot(da['Runs'], bins=15, kde=True) 
m.title('Distribution of Runs Scored') 
m.show() 
m.figure(figsize=(18,10)) 
s.barplot(data=da,x='Year',y='Runs',palette='viridis') 
m.title('Batting Scores Over the Years') 
m.xlabel('Year');m.ylabel('Runs') 
m.xticks(rotation=45);m.show() 
m.figure(figsize=(18,10)) 
s.heatmap(data=da.corr(),annot=True,cmap='crest') 
m.title("Heatmap on DHONI's stats") 
m.show() 

