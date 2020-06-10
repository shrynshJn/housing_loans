from bangalore.usethis import predict_price as bangalore
from chennai.usethis import predict_price as chennai
from delhi.usethis import predict_price as delhi
from mumbai.usethis import predict_price as mumbai
from flask_cors import CORS, cross_origin
from flask import Flask, request
app = Flask(__name__)
CORS(app, resource={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/predict/mumbai', methods=['POST'])
@cross_origin(supports_credentials=True)
def mumbai_predict():
    data = request.get_json()
    localality = data['locality']
    bed = int(data['bed'])
    area = float(data['area'])
    furnished = data['furnished']
    types=data['types']
    bath=int(data['bath'])
    floor_count=int(data['floor_count'])
    floor_num = int(data['floor_num'])
    price = mumbai(localality, bed, area, furnished, types, bath, floor_count, floor_num)
    return {'price': price}

@app.route('/predict/delhi', methods=['POST'])
@cross_origin(supports_credentials=True)
def delhi_predict():
    data = request.get_json()
    bhk = int(data['bhk'])
    localality = data['locality']
    area = float(data['area'])
    bath=int(data['bath'])
    furnished = data['furnished']
    parking = int(data['parking'])
    status = data['Ready_to_move']
    transaction= data['transaction']
    types=data['types']
    price = delhi(bhk, localality, area, bath, furnished, parking, status, transaction, types)
    return {'price': price}


@app.route('/predict/chennai', methods=['POST'])
@cross_origin(supports_credentials=True)
def chennai_predict():
    data = request.get_json()
    location = data['location']
    sqft = float(data['sqft'])
    types=data['types']
    bath = int(data['bath'])
    bhk = int(data['bhk'])
    price = chennai(location, sqft, types, bath, bhk)
    return {'price': price}

@app.route('/predict/bangalore', methods=['POST'])
@cross_origin(supports_credentials=True)
def bangalore_predict():
    data = request.get_json()
    location = data['location']
    sqft = float(data['sqft'])
    bath = int(data['bath'])
    balcony = int(data['balcony'])
    bhk = int(data['bhk'])
    price = bangalore(location, sqft,  bath, balcony, bhk)
    return {'price': price}
