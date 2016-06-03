#!usr/bin/python
#coding=utf8
from flask import Flask,request,render_template, jsonify
from dataSource import stockK


app = Flask(__name__)

# 修饰器
@app.route('/')
# 视图函数
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return jsonify({'name' : name , 'age' : '123'})
#     return '<h1>hello,%s!' % name

@app.route('/stock/<code>')
def stockInfo(code):
    print request.json 
    stock = stockK('399001')
    return render_template('stock.html',code = code , k = stock.K() , d = stock.D(),status = stock.kdStatus())

if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port= 8080 ,debug=True)

