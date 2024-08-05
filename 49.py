import pandas as p 
da=p.read_csv("C:\\ab\\archive (12).zip") 
da.info() 
 
#PRE_PROCESSING 
miss=da.isna().sum() 
print("\nMissing Values:\n",miss) 
da.dropna(inplace=True) 
print("\nMissing Values:\n",da.isna().sum())
import matplotlib.pyplot as m 
import seaborn as s 
 
m.figure(figsize=(18,10)) 
s.countplot(data=da, x='State_Name') 
m.title("Sates Which grow Crops") 
m.xticks(rotation=90) 
m.show()
m.figure(figsize=(18,10)) 
s.countplot(data=da,x='Crop_Year') 
m.title('Crops Grown In an year') 
m.xticks(rotation=90) 
m.show() 
 
m.figure(figsize=(12, 6)) 
s.barplot(x=da['Crop_Year'], y=da['Production'],data=da) 
m.title('Rice Production by Year') 
m.xlabel('Year') 
m.ylabel('Production (Metric Tons)') 
m.xticks(rotation=45) 
m.tight_layout() 
m.show() 
 
sn=da.select_dtypes(exclude=['object']) 
s.heatmap(data=sn.corr(),annot=True,cmap='coolwarm') 
m.show()
from sklearn.preprocessing import LabelEncoder 
from sklearn.model_selection import train_test_split 
 
#Transformation 
categorical_columns = ['State_Name','District_Name','Season','Crop'] 
label_encoders = {} 
 
for column in categorical_columns: 
    label_encoders[column] = LabelEncoder() 
    da[column] = label_encoders[column].fit_transform(da[column]) 
 
X = da.drop('Production', axis=1)   
y = da['Production'] 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42) 
print("Train set:", X_train.shape, y_train.shape) 
print("Test set:", X_test.shape, y_test.shape)