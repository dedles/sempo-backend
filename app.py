from flask import Flask, request, jsonify
import os

from web3.auto import w3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

@app.route('/create', methods=['POST'])
def post():
    acct = w3.eth.account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
    acct.address
    return jsonify({
        'amazebert': acct.address
    })



if __name__ == '__main__':
    app.run(debug=True)

