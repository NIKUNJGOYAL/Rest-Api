import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store,StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE URI']='postgres://qvobgdqliizdqh:320b5dbebc0df4ed0fd90434abbfbcca488569479c0df42ba74ac0cbf1d49043@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d8n6h3ekfp2jne'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='jose'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)
