#!usr/bin/python
#coding=utf-8
from flask import Flask
from flask import jsonify
from flask import request
from posix import abort
from pip.status_codes import SUCCESS
from boto.gs.cors import METHOD
from pip._vendor.distlib._backport.tarfile import TUREAD

root= Flask(__name__)
app = Flask(__name__)
post_test = Flask(__name__)

@root.route('/')
def welcome():
    return "Welcome to stock system!"
#
# code price 
stocks = [{'name' : '123','price':'1504'}]

# curl -i -H "Content-Type:application/json" -X POST 'http://127.0.0.1:5000/stock' -d '{"name":"深圳成指","price":"9675"}'

@post_test.route('/stock',methods = ['POST'])
def addStock():
#     print(stocks)
    print('json = ' + request.json + 'args = ' + request.args)
    if not request.json or not 'name' in request.json  or not 'price' in request.json:
#         abort(400)
        print('400')
    stock = {'name' : request.args['name'],
             'price' : request.args['price'] 
             }
    
    stocks.append(stock)
    return 'Success'
    
# curl -X get 'http://127.0.0.1:5000/stock?name=123'
@app.route('/stock',methods = ['GET'])
def get_stocks():
    if not request.json:
        abort(400)
    get_name = request.json['name']
    stock = filter(lambda s:s['name'] == get_name ,stocks)
    if len(stock) == 0:
        abort(400)
    return jsonify({'stock': stock[0]})

# root.run(debug = True)
# app.run(debug = True)
# post_test.run( debug = True)
# host = '172.30.8.82',port = 1234 , 
