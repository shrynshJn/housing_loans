import pickle
import numpy as np
with open('delhi.pickle','rb') as f:
    model = pickle.load(f)

with open('locations2.txt','r') as file:
    locs = file.read()

l = locs.split('@')
X = np.array(l)

def predict_price(bhk,locality,area=1000,bath=2,furnished='Semi-Furnished',parking=1,status='Ready_to_move',transaction='Resale',types='Apartment'):
    loc_ind = np.where(X == locality)[0][0]
    fur_ind = np.where(X == furnished)[0][0]
    type_ind = np.where(X == types)[0][0]
    trans_ind = np.where(X == transaction)[0][0]
    status_ind = np.where(X == status)[0][0]
    
    x = np.zeros(len(X))
    x[0] = area
    x[1] = bhk
    x[2] = bath
    x[3] = parking
    if loc_ind>=0:
        x[loc_ind] = 1
        x[fur_ind] = 1
        x[type_ind] = 1
        x[trans_ind] = 1
        x[status_ind] = 1
    return model.predict([x])[0]

print(predict_price(3,'Rohini',1200,3,'Unfurnished'))