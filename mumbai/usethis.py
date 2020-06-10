import pickle
import numpy as np
with open('./mumbai/mumbai.pickle','rb') as f:
    model = pickle.load(f)

with open('./mumbai/locations2.txt','r') as file:
    locs = file.read()

l = locs.split('@')
X = np.array(l)

def predict_price(locality,bed,area=1000,furnished='Semi-Furnished',types="Penthouse",bath=2,floor_count=1,floor_num=0):
    loc_ind = np.where(X == locality)[0][0]
    fur_ind = np.where(X == furnished)[0][0]
    type_ind = np.where(X == types)[0][0]
    
    x = np.zeros(len(X))
    x[0] = area
    x[1] = bath
    x[2] = bed
    x[3] = floor_count
    x[4] = floor_num
    if loc_ind>=0:
        x[loc_ind] = 1
        x[fur_ind] = 1
        x[type_ind] = 1
    return model.predict([x])[0]