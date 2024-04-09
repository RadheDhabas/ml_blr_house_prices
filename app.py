from flask import Flask, request, jsonify
import util

app = Flask(__name__)
@app.route('/', methods=['GET'])
def blr_home_prices():
    return 'Bangalore Home Prices Model'
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    with open("./model files/columns.json", "r") as f:
        data_columns = json.load(f)['data_columns']
        location = data_columns[3:]

    response = jsonify({
        'locations': location
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
