import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df1 = pd.read_csv('Bengaluru_House_Data.csv')

df1.drop(['availability','area_type','society'],axis=1,inplace=True)
df1.dropna(inplace=True)

def cla_rooms(abc):
    return int(abc[0])

df1['rooms'] = df1['size'].apply(cla_rooms)

def conv_flt(abc):
    try:
        return float(abc)
    except:
        try:
            l = abc.split('-')
            return (float(l[0]) + float(l[1]))/2
        except:
            return 0

df1['total_sqft'] = df1['total_sqft'].apply(conv_flt)

df1['price_per_sqft'] = df1['price']*100000/df1['total_sqft']


df1.drop(['size'],inplace=True,axis=1)

df1

l = list(df1['location'])

def if_other(abc):
    count = 0
    for i in range(len(l)):
        if abc == l[i]:
            count=count+1
    
    if count<10:
        return 'other'
    else:
        return abc

df1['location'] = df1['location'].apply(if_other)

df1 = df1[~(df1['total_sqft']/df1['rooms']<300)]

df1 = df1[~(df1['bath']>df1['rooms']+2)]

df1 = df1[~(df1['balcony']>df1['rooms']+1)]

def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats={}
        for bhk,bhk_df in location_df.groupby('rooms'):
            bhk_stats[bhk] = {
                'mean' : np.mean(bhk_df.price_per_sqft),
                'std' : np.std(bhk_df.price_per_sqft),
                'count': bhk_df.shape[0]
            }
        for bhk,bhk_df in location_df.groupby('rooms'):
            stats = bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indices = np.append(exclude_indices,bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
    return df.drop(exclude_indices,axis='index')

df1 = remove_bhk_outliers(df1)

dums = pd.get_dummies(df1['location'])

df1 = pd.concat([df1,dums],axis = 1)

df1.drop(['location'],axis=1,inplace=True)

df1.drop(7242,inplace=True)
df1.drop(11748,inplace=True)
df1.drop(7657,inplace=True)



X = df1.drop('price',axis=1)
y = df1['price']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3 , random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

print(model.score(X_test,y_test))

def predict_price(location,sqft,bath,balcony,bhk):
    loc_ind = np.where(X.columns == location)[0][0]
    
    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_ind>=0:
        x[loc_ind] = 1
        
    return model.predict([x])[0]

import pickle
with open('bangalore.pickle','wb') as f:
    pickle.dump(model,f)
X = list(X.columns)
X = ','.join(X)
with open('locations.txt','w') as file:
    file.write(X)