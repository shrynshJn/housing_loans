import pickle
import numpy as np
with open('./bangalore/bangalore.pickle','rb') as f:
    model = pickle.load(f)

with open('./bangalore/locations.txt','r') as file:
    locs = file.read()

l = locs.split(',')

X = np.array(l)

def predict_price(location,sqft,bath,balcony,bhk):
    print(X)
    print(location)
    loc_ind = np.where(X == location)
    print(loc_ind)
    loc_ind = loc_ind[0][0]
    print(loc_ind)
    
    x = np.zeros(len(X))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_ind>=0:
        x[loc_ind] = 1
        
    return model.predict([x])[0]
