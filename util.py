import pickle
import json
import numpy as np

__model = None
__data_columns = None
__locations = None

def get_estimated_price(location,sqft,bhk,bath,model,data_columns):
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

def get_locations():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./model files/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    global __model
    if __model is None:
        with open('./model files/bangalore_home_price_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    return __model,__locations,__data_columns
