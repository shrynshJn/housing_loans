import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv('MagicBricks.csv')
def Rohini(abc):
    ls = abc.split(" ")
    if "Rohini" in ls:
        return "Rohini"
    else:
        return abc
def Lajpat(abc):
    ls = abc.split(" ")
    if "Lajpat" in ls:
        return "Lajpat Nagar"
    else:
        return abc
def Dwarka(abc):
    ls = abc.split(" ")
    if "Dwarka" in ls:
        return "Dwarka"
    else:
        return abc
def Budh(abc):
    if "Budh Vihar" in abc:
        return "Budh Vihar"
    else:
        return abc
def Patel(abc):
    ls = abc.split(" ")
    if "Patel" in ls:
        return "Patel Nagar"
    else:
        return abc
def Uttam(abc):
    ls = abc.split(" ")
    if "Uttam" in ls:
        return "Uttam Nagar"
    else:
        return abc
def gk(abc):
    if "Greater Kailash 1" in abc:
        return "Greater Kailash 1"
    elif "Greater Kailash 2" in abc:
        return "Greater Kailash 2"
    elif "Greater Kailash 3" in abc:
        return "Greater Kailash 3"
    elif "Greater Kailash 4" in abc:
        return "Greater Kailash 4"
    elif "Greater Kailash" in abc:
        return "Greater Kailash"
    
    else:
        return abc
def karol(abc):
    if "Karol Bagh" in abc:
        return "Karol Bagh"
    else:
        return abc
def okhla(abc):
    if "Okhla" in abc:
        return "Okhla"
    else:
        return abc
def Najaf(abc):
    if "Najafgarh" in abc:
        return "Najafgarh"
    else:
        return abc
def Vasant(abc):
    if "Vasant Vihar" in abc:
        return "Vasant Vihar"
    else:
        return abc
def vkunj(abc):
    if "Vasant Kunj" in abc:
        return "Vasant kunj"
    else:
        return abc
def nfc(abc):
    if "New Friends Colony" in abc:
        return "New Friends Colony"
    else:
        return abc
def Shahdara(abc):
    if "Shahdara" in abc:
        return "Shahadara"
    else:
        return abc
def Laxmi(abc):
    if "Laxmi Nagar" in abc:
        return "Laxmi Nagar"
    else:
        return abc
def Saket(abc):
    if "Saket" in abc:
        return "Saket"
    else:
        return abc
def Chandni(abc):
    if "Chandni Chowk" in abc:
        return "Chandni Chowk"
    else:
        return abc
def safe(abc):
    if "Safdarjung Enclave" in abc:
        return "Safdarjung Enclave"
    else:
        return abc
def mind(abc):
    if "mind" in abc:
        return "mind"
    else:
        return abc
def pasch(abc):
    if "Paschim Vihar Block B2" in abc:
        return "Paschim Vihar Block B2"
    elif "Paschim Vihar Block B1" in  abc:
        return "Paschim Vihar Block B1"
    elif "Paschim Vihar Block B3" in  abc:
        return "Paschim Vihar Block B3"
    elif "Paschim Vihar Block B4" in  abc:
        return "Paschim Vihar Block B4"
    elif "Paschim Vihar" in  abc:
        return "Paschim Vihar"
    else:
        return abc
def Razadpur(abc):
    if "Razapur Khurd" in abc:
        return "Razapur Khurd"
    else:
        return abc
def cwg(abc):
    if "Commonwealth Games Village 2010" in abc:
        return "Commonwealth Games Village 2010"
    else:
        return abc
def Alaknanda(abc):
    if "Alaknanda" in abc:
        return "Alaknanda"
    else:
        return abc
def sarita(abc):
    if "Sarita Vihar" in abc:
        return "Sarita Vihar"
    else:
        return abc
def sultan(abc):
    if "Sultanpur" in abc:
        return "Sultanpur"
    else:
        return abc
def Chattarpur(abc):
    if "Chattarpur" in abc or "Chhattarpur" in abc:
        return "Chattarpur"
    else:
        return abc
def Mehrauli(abc):
    if "Mehrauli" in abc:
        return "Mehrauli"
    else:
        return abc
def Mahavir(abc):
    if "Mahavir Enclave" in abc:
        return "Mahavir Enclave"
    else:
        return abc
def Narela(abc):
    if "Narela" in abc:
        return "Narela"
    else:
        return abc
def Malviya(abc):
    if "Malviya Nagar" in abc:
        return "Malviya Nagar"
    else:
        return abc
def Dilshad(abc):
    if "Dilshad Garden" in abc:
        return "Dilshad Garden"
    else:
        return abc
def Vasundhara(abc):
    if "Vasundhara Enclave" in abc:
        return "Vasundhara Enclave"
    else:
        return abc
def Kirti(abc):
    if "Kirti Nagar" in abc:
        return "Kirti Nagar"
    else:
        return abc
def Sheik(abc):
    if "Sheikh Sarai Phase 1" in abc:
        return "Sheikh Sarai Phase 1"
    elif "Sheikh Sarai Phase 2" in  abc:
        return "Sheikh Sarai Phase 2"
    elif "Sheikh Sarai" in  abc:
        return "Sheikh Sarai"
    else:
        return abc
def Punjabi(abc):
    if "Punjabi Bagh" in abc:
        return "Punjabi Bagh"
    else:
        return abc
def Kalkaji(abc):
    if "Kalkaji" in abc:
        return "Kalkaji"
    else:
        return abc
def Hauz(abc):
    if "Hauz Khas" in abc:
        return "Hauz Khas"
    else:
        return abc
def Chittaranjan(abc):
    if "Chittaranjan Park" in abc:
        return "Chittaranjan Park"
    else:
        return abc

df['Locality'] = df['Locality'].apply(Rohini)
df['Locality'] = df['Locality'].apply(Lajpat)
df['Locality'] = df['Locality'].apply(Dwarka)
df['Locality'] = df['Locality'].apply(Budh)
df['Locality'] = df['Locality'].apply(Patel)
df['Locality'] = df['Locality'].apply(Uttam)
df['Locality'] = df['Locality'].apply(gk)
df['Locality'] = df['Locality'].apply(karol)
df['Locality'] = df['Locality'].apply(okhla)
df['Locality'] = df['Locality'].apply(Najaf)
df['Locality'] = df['Locality'].apply(Vasant)
df['Locality'] = df['Locality'].apply(vkunj)
df['Locality'] = df['Locality'].apply(nfc)
df['Locality'] = df['Locality'].apply(Shahdara)
df['Locality'] = df['Locality'].apply(Laxmi)
df['Locality'] = df['Locality'].apply(Saket)
df['Locality'] = df['Locality'].apply(Chandni)
df['Locality'] = df['Locality'].apply(safe)
df['Locality'] = df['Locality'].apply(pasch)
df['Locality'] = df['Locality'].apply(mind)
df['Locality'] = df['Locality'].apply(Razadpur)
df['Locality'] = df['Locality'].apply(Alaknanda)
df['Locality'] = df['Locality'].apply(sarita)
df['Locality'] = df['Locality'].apply(cwg)
df['Locality'] = df['Locality'].apply(sultan)
df['Locality'] = df['Locality'].apply(Chattarpur)
df['Locality'] = df['Locality'].apply(Mehrauli)
df['Locality'] = df['Locality'].apply(Mahavir)
df['Locality'] = df['Locality'].apply(Narela)
df['Locality'] = df['Locality'].apply(Malviya)
df['Locality'] = df['Locality'].apply(Dilshad)
df['Locality'] = df['Locality'].apply(Vasundhara)
df['Locality'] = df['Locality'].apply(Kirti)
df['Locality'] = df['Locality'].apply(Sheik)
df['Locality'] = df['Locality'].apply(Punjabi)
df['Locality'] = df['Locality'].apply(Kalkaji)
df['Locality'] = df['Locality'].apply(Hauz)
df['Locality'] = df['Locality'].apply(Chittaranjan)


l = list(df['Locality'])

def if_other(abc):
    count = 0
    for i in range(len(l)):
        if abc==l[i]:
            count=count+1
    if count<2:
        return "Other"
    else:
        return abc


df['Locality'] = df['Locality'].apply(if_other)

df.dropna(inplace=True)

df.drop(df[df['Area']>8000].index,inplace=True)
df.drop(df[df['Parking']>3].index,inplace=True)
df.drop(df[df['Price']>200000000].index,inplace=True)
df.drop(df[df['Price']<1500000].index,inplace=True)
df.drop(df[df['BHK']>5].index,inplace=True)
df.drop(df[df['Bathroom']>5].index,inplace=True)
df.drop(df[df['Per_Sqft']>100000].index,inplace=True)
x = df[df['Price']>6900000]
df.drop(x[x['BHK']==1].index,inplace=True)
df.drop('Per_Sqft',axis=1,inplace=True)


dum_fur = pd.get_dummies(df['Furnishing'])
dum_loc = pd.get_dummies(df['Locality'])
dum_Status = pd.get_dummies(df['Status'])
dum_trans = pd.get_dummies(df['Transaction'])
dum_type = pd.get_dummies(df['Type'])


df = pd.concat([df,dum_fur,dum_loc,dum_Status,dum_trans,dum_type],axis=1)


df.drop('Furnishing',axis=1,inplace=True)
df.drop('Locality',axis=1,inplace=True)
df.drop('Type',axis=1,inplace=True)
df.drop('Status',axis=1,inplace=True)
df.drop('Transaction',axis=1,inplace=True)


X = df.drop('Price',axis=1)
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train,y_train)
preds = model.predict(X_test)

print(model.score(X_test,y_test))

with open('delhi.pickle','wb') as f:
    pickle.dump(model,f)
X = list(X.columns)
X = '@'.join(X)
with open('locations2.txt','w') as file:
    file.write(X)

