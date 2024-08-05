import missingno as ms 
ti_d=ms.read_csv("C:\\ab\\Titanic.csv") 
 
#Box Plot 
ms.bar(ti_d) 
ms.title("Missing values in Dataset") 
ms.show() 
 
#Matrix Plot 
ms.matrix(ti_d) 
ms.title('Missing Values Matrix Plot') 
ms.show() 
 
#Removing Null Objects 
print("Before Droping Objects:\n") 
ti_d.info() 
ti_d=ti_d.dropna(axis=0) 
print("\n\nAfter Droping objects:\n") 
ti_d.info() 
 
#Removing Null Attributes 
print("\nBefore Droping Attributes:\n") 
ti_d.info() 
ti=ti_d.dropna(axis=1) 
print("\n\nAfter Droping Attributes:\n") 
ti.info() 
 
#Imputing Missing value of Age column through Mean 
print("\n\nAge column before imputing:\n") 
ti_d['Age'].info() 
ti_ag=ti_d['Age'].fillna(ti_d['Age'].mean()) 
print("\n\nAfter Imputing:\n") 
ti_ag.info()