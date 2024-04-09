import pickle
import json
import numpy as np

model = None
data_columns = None
locations = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1
    return round(model.predict([x])[0],2)


def load_saved_artifacts():
    with open("./model files/columns.json", "r") as f:
        global model
        global data_columns
        global locations
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]  # first 3 columns are sqft, bath, bhk
        with open('./model files/bangalore_home_price_model.pickle', 'rb') as f:
            model = pickle.load(f)
    
    # return model,locations,data_columns
