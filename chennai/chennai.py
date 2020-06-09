import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('chennai.csv')

df.drop('SALE_COND',axis=1,inplace=True)
df.drop('PARK_FACIL',axis=1,inplace=True)
df.drop('UTILITY_AVAIL',axis=1,inplace=True)
df.drop('STREET',axis=1,inplace=True)
df.drop('MZZONE',axis=1,inplace=True)
df.drop('QS_ROOMS',axis=1,inplace=True)
df.drop('QS_BATHROOM',axis=1,inplace=True)
df.drop('QS_BEDROOM',axis=1,inplace=True)
df.drop('PRT_ID',axis=1,inplace=True)
df.drop('DIST_MAINROAD',inplace=True,axis=1)
df.drop('COMMIS',inplace=True,axis=1)
df.drop('N_ROOM',inplace=True,axis=1)
df.drop('QS_OVERALL',axis=1,inplace=True)
df.dropna(inplace=True)

def types(abc):
    if abc == 'Commercial' or abc=='Comercial':
        return 'Commercial'
    elif abc == 'Others' or abc=='Other':
        return 'Others'
    else:
        return abc
def area(abc):
    if abc == 'Anna Nagar' or abc=='Ana Nagar' or abc=='Ann Nagar':
        return 'Anna Nagar'
    elif abc == 'Adyar' or abc=='Adyr':
        return 'Adyar'
    elif abc == 'Velachery' or abc=='Velchery':
        return 'Velachery'
    elif abc == 'Chrompet' or abc=='Chormpet' or abc=='Chrompt' or abc=='Chrmpet':
        return 'Chrompet'
    elif abc == 'KK Nagar' or abc=='KKNagar':
        return 'KK Nagar'
    elif abc == 'TNagar' or abc=='T Nagar':
        return 'T Nagar'
    elif abc == 'Karapakkam' or abc=='Karapakam':
        return 'Karapakkam'
    else:
        return abc


df['BUILDTYPE'] = df['BUILDTYPE'].apply(types)
df['AREA'] = df['AREA'].apply(area)


dums_area = pd.get_dummies(df['AREA'])
dums_type = pd.get_dummies(df['BUILDTYPE'])

df = pd.concat([df,dums_area,dums_type],axis=1)

df.drop('AREA',inplace=True,axis=1)
df.drop('BUILDTYPE',inplace=True,axis=1)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df.drop('SALES_PRICE',axis=1)
y = df['SALES_PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression(abs)

model.fit(X_train,y_train)

import pickle
with open('chennai.pickle','wb') as f:
    pickle.dump(model,f)
X = list(X.columns)
X = '@'.join(X)
with open('locations.txt','w') as file:
    file.write(X)