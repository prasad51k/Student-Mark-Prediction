import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df_train=pd.read_csv(r'C:\Users\venkatesh\Downloads\archive\train.csv')

df_test=pd.read_csv(r'C:\Users\venkatesh\Downloads\archive\test.csv')

#merge both train and test data
df=df_train.append(df_test)

df.drop(['User_ID'],axis=1,inplace=True)

#Handle categorical feature Gender
#map function will do it will map based on the condition
df['Gender']=df['Gender'].map({'F':0,'M':1})

#Handle categorical feature Age
df['Age'].unique()

#pd.get_dummies(df['Age'],drop_first=True)
df['Age']=df['Age'].map({'0-17':1,'18-25':2,'26-35':3,'36-45':4,'46-50':5,'51-55':6,'55+':7})

#fixing categorical city_categorical
df_city=pd.get_dummies(df['City_Category'],drop_first=True)

df=pd.concat([df,df_city],axis=1)
df.drop(['City_Category'],axis=1,inplace=True)

#replace the missing values with mode for feature 'Product_Category_2'
df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])

#df['Product_Category_2'].isnull().sum()

#replace the missing values with mode for feature 'Product_Category_3'
df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])
#df['Product_Category_3'].isnull().sum()

#df['Stay_In_Current_City_Years'].unique()
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')

#convert object into integers
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)  

df['B']=df['B'].astype(int)
df['C']=df['C'].astype(int)

#visualisation (men vs purchase)
sns.barplot('Age','Purchase',hue='Gender',data=df)
#observation
#purchasing of men is higher than women

#visualisation of purchase with occupation
sns.barplot('Occupation','Purchase',hue='Gender',data=df) 

sns.barplot('Product_Category_1','Purchase',hue='Gender',data=df) 

sns.barplot('Product_Category_1','Purchase',hue='Gender',data=df) 

#feature scaling
#df_test=df[df['Purchase'].isnull()]
#df_train=df[df['Purchase'].isnull()]

#X=df_train.drop('Purchase',axis=1)

#y=df['Purchase']


















