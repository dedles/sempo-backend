from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from web3.auto import w3

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

@app.route('/create', methods=['POST'])
def post():
    name = request.json['name']
    acct = w3.eth.account.create(name)
    
    return jsonify({
        "name": name,
        "address": acct.address,
        "key": acct.key.hex(),
        "privateKey": acct.privateKey.hex(),
    })



if __name__ == '__main__':
    app.run(debug=True)

