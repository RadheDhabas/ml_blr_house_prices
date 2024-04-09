from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.json['total_sqft'])
    location = request.json['location']
    bhk = int(request.json['bhk'])
    bath = int(request.json['bath'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath,model,data_columns)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    model, locations, data_columns = util.load_saved_artifacts()
    app.run()
