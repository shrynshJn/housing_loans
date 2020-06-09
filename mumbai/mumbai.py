
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv('prop_data_clean.csv')

df.drop(df[df['city'].isna()==True].index,inplace=True)
df.drop(df[df['area'].isna()==True].index,inplace=True)
df.drop(df[df['bathroom_num'].isna()==True].index,inplace=True)
df.drop(df[df['bedroom_num'].isna()==True].index,inplace=True)
df.drop(df[df['furnishing'].isna()==True].index,inplace=True)
df.drop(df[df['price'].isna()==True].index,inplace=True)
df.drop(df[df['trans'].isna()==True].index,inplace=True)
df.drop(df[df['type'].isna()==True].index,inplace=True)

df.drop('city',axis=1,inplace=True)
df.drop('dev_name',axis=1,inplace=True)
df.drop('desc',axis=1,inplace=True)
df.drop('id',axis=1,inplace=True)
df.drop('url',axis=1,inplace=True)
df.drop('user_type',axis=1,inplace=True)
df.drop('trans',axis=1,inplace=True)
df.drop('id_string',axis=1,inplace=True)
df.drop('latitude',axis=1,inplace=True)
df.drop('post_date',axis=1,inplace=True)
df.drop('poster_name',axis=1,inplace=True)
df.drop('longitude',axis=1,inplace=True)
df.drop('project',axis=1,inplace=True)
df.drop('title',axis=1,inplace=True)
df.drop(df[df['floor_count'].isna()==True].index,inplace=True)
df.drop(df[df['floor_num'].isna()==True].index,inplace=True)

df.drop(df[df['floor_count']<df['floor_num']].index,inplace=True)
df.shape

df.groupby('locality').count()

l = list(df['locality'])
def other_locs(abc):
    count = 0
    for i in range(len(l)):
        if abc == l[i]:
            count=count+1
        
    if count<10:
        return "Other"
    else:
        return abc

df['locality'] = df['locality'].apply(other_locs)

furn = pd.get_dummies(df['furnishing'])
locality = pd.get_dummies(df['locality'])
types = pd.get_dummies(df['type'])

df = pd.concat([df,furn,locality,types],axis=1)

df.drop('furnishing',axis=1,inplace=True)
df.drop('locality',axis=1,inplace=True)
df.drop('type',axis=1,inplace=True)

df.drop(df[df['bedroom_num']<df['bathroom_num']-1].index,inplace=True)

mean_price = df['price'].mean()
df.drop(df[df['price']<mean_price-75000].index,inplace=True)
df.drop(df[df['price']>mean_price+75000].index,inplace=True)
df['price'].describe()


X = df.drop('price',axis=1)
y = df['price']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)


from sklearn.metrics import r2_score,mean_squared_error

#print(model.score(X_test,y_test))


with open('mumbai.pickle','wb') as f:
    pickle.dump(model,f)
X = list(X.columns)
X = '@'.join(X)
with open('locations2.txt','w') as file:
    file.write(X)