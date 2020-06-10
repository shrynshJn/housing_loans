from bangalore.usethis import predict_price as bangalore
from chennai.usethis import predict_price as chennai
from delhi.usethis import predict_price as delhi
from mumbai.usethis import predict_price as mumbai
from flask_cors import CORS, cross_origin
from flask import Flask, request
app = Flask(__name__)
CORS(app, resource={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

mumbai_data = {}
delhi_data = {}
chennai_data = {}
bangalore_data = {}
def load_mumbai_data():
    with open('mumbai_types.txt', 'r') as type_file:
        types = type_file.read()
        mumbai_data['types'] = types.split('@')
    with open('mumbai_locs.txt', 'r') as loc_file:
        locs = loc_file.read()
        mumbai_data['locality'] = locs.split('@')
    with open('mumbai_furnished.txt') as furnished_file:
        furnished = furnished_file.read()
        mumbai_data['furnished'] = furnished.split('@')

def load_delhi_data():
    with open('delhi_types.txt', 'r') as type_file:
        types = type_file.read()
        delhi_data['types'] = types.split('@')
    with open('delhi_locs.txt', 'r') as loc_file:
        locs = loc_file.read()
        delhi_data['locality'] = locs.split('@')
    with open('delhi_furnished.txt') as furnished_file:
        furnished = furnished_file.read()
        delhi_data['furnished'] = furnished.split('@')
    with open('delhi_status.txt', 'r') as status_file:
        status = status_file.read()
        delhi_data['status'] = status.split('@')
    with open('delhi_transactions.txt', 'r') as transaction_file:
        transactions = transaction_file.read()
        delhi_data['transactions'] = transactions.split('@')

def load_chennai_data():
    with open('chennai_types.txt', 'r') as type_file:
        types = type_file.read()
        chennai_data['types'] = types.split('@')
    with open('chennai_locs.txt', 'r') as loc_file:
        locs = loc_file.read()
        chennai_data['location'] = locs.split('@')

def load_bangalore_data():
    with open('bangalore_locs.txt', 'r') as loc_file:
        locs = loc_file.read()
        bangalore_data['location'] = locs.split(',')

load_mumbai_data()
load_delhi_data()
load_chennai_data()
load_bangalore_data()

@app.route('/data/mumbai', methods=['GET'])
@cross_origin(supports_crentials=True)
def get_mumbai():
    return mumbai_data

@app.route('/data/delhi', methods=['GET'])
@cross_origin(supports_crentials=True)
def get_delhi():
    return delhi_data

@app.route('/data/chennai', methods=['GET'])
@cross_origin(supports_crentials=True)
def get_chennai():
    return chennai_data

@app.route('/data/banaglore', methods=['GET'])
@cross_origin(supports_crentials=True)
def get_banagalore():
    return bangalore_data

@app.route('/predict/mumbai', methods=['POST'])
@cross_origin(supports_credentials=True)
def mumbai_predict():
    data = request.get_json()
    locality = data['locality']
    bed = int(data['bed'])
    area = float(data['area'])
    furnished = data['furnished']
    types=data['types']
    bath=int(data['bath'])
    floor_count=int(data['floor_count'])
    floor_num = int(data['floor_num'])
    price = mumbai(locality, bed, area, furnished, types, bath, floor_count, floor_num)
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
