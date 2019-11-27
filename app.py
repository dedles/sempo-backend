import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from web3.auto import w3
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from functions import convert_key_to_emoji


app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    private_key = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), unique=True)

    def __init__(self, name, private_key, address):
        self.name = name 
        self.private_key = private_key
        self.address = address

# Account Schema

class AccountSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'private_key', 'address')

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

@app.route('/create', methods=['POST'])
def post():
    name = request.json['name']
    acct = w3.eth.account.create(name)
    private_key = acct.privateKey.hex()
    address = acct.address

    new_account = Account(name, private_key, address)

    db.session.add(new_account)
    db.session.commit()

    emoji = convert_key_to_emoji(new_account.private_key)

    return jsonify({
        'address': new_account.address,
        'emoji_key': emoji,
        'name': new_account.name,
        "id": new_account.id
    })

@app.route('/accounts', methods=['GET'])
def accounts():
    all_accounts = Account.query.all()
    result = accounts_schema.dump(all_accounts)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
