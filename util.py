import pickle
import json
import numpy as np

def get_estimated_price(location,sqft,bhk,bath):
    try:
        location_index = data_columns.index(location.lower())
    except:
        location_index = -1
    model,data_columns = load_saved_artifacts()[0],load_saved_artifacts()[2]
    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location_index>=0:
        x[location_index] = 1
    return round(model.predict([x])[0],2)

def get_locations():
    locations = load_saved_artifacts()[1]
    return locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    
    with open("./model files/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        locations = data_columns[3:]  # first 3 columns are sqft, bath, bhk
    
    with open('./model files/bangalore_home_price_model.pickle', 'rb') as f:
        model = pickle.load(f)
    print("loading saved artifacts...done")
    return [model,locations,data_columns]
