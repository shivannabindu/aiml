#bar graph
from matplotlib import pyplot as p 
pro_na=["Intel","AMD","Snapdragon","Tensor"] 
use=[200,100,250,50]  
p.bar(pro_na,use,color='black',width=0.2) 
p.xlabel("Processors"),p.ylabel("No of Users") 
p.title("Processor Users in a Community") 
p.show()
#pie graph
from matplotlib import pyplot as pi 
us=[12,32,16,45] 
la=["Asus","Dell","Lenovo","HP"] 
e=[0,0,0,0.04] 
c=["g","c","#8B0000","#473C8B"] 
pi.pie(us,labels=la,startangle=270, 
explode=e,colors=c,autopct='%1.2f%%') 
pi.show()
#line graph
from matplotlib import pyplot as p 
Q=["Q1","Q2","Q3","Q4"] 
ssd=[200,230,350,400] 
hdd=[250,240,320,250] 
p.plot(Q,ssd,'^-',color='black') 
p.plot(Q,hdd,'o-.r') 
p.xlabel("Quarters in 2022"),p.ylabel("Sales Units") 
p.title("Sdd & Hdd sales in store") 
p.legend(['Ssd','Hdd']) 
p.show() 
#histo graph
from matplotlib import pyplot as p 
import numpy as n 
x=n.random.normal(180,5,200) 
p.hist(x,color='k') 
p.xlabel("Height in cm"),p.ylabel("People") 
p.title("Height of 200 people") 
p.show() 
#scatter graph
from matplotlib import pyplot as p 
x=[2,6,8,7,3,2,5] 
y=[6,7,9,7,5,3,2] 
c=['k','b'] 
p.scatter(x,y,label='Value of x y',color='k') 
p.xlabel('x') 
p.ylabel('y') 
p.legend() 
p.show() 
 

