import pickle
import numpy as np
with open('./chennai/chennai.pickle','rb') as f:
    model = pickle.load(f)

with open('./chennai/locations.txt','r') as file:
    locs = file.read()

l = locs.split('@')

X = np.array(l)

def predict_price(location,sqft,types="Commercial",bath=1,bhk=1):
    loc_ind = np.where(X == location)[0][0]
    loc_types = np.where(X == types)[0][0]
    
    x = np.zeros(len(X))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_ind>=0:
        x[loc_ind] = 1
    if loc_types>=0:
        x[loc_types] = 1
        
    return model.predict([x])[0]

print(predict_price('KK Nagar',500,'Commercial',2,2))