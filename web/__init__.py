#!usr/bin/python
#coding=utf8
from flask import Flask,request,render_template, jsonify
from dataSource import stockK


app = Flask(__name__)

# 修饰器
@app.route('/')
# 视图函数
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    code = request.args.get('code','399001')
    ktype = request.args.get('ktype','D')
    stock = stockK(code=code ,ktype = ktype)
    
# 以下是可以获得的数据
    k = stock.K()
    d = stock.D()
    statusKD = stock.kdStatus()
    boll= stock.BOLL()
    
    json = jsonify({'code' : code ,'K': k,'D':d,'statusKD':statusKD,
                    'boll' : boll})
    return json
    
@app.route('/stock/<code>')
def stockInfo(code):
    print(request.json)
    stock = stockK('399001')
    return render_template('stock.html',code = code , k = stock.K() , d = stock.D(),status = stock.kdStatus())

if __name__ == '__main__':
    app.run(host = '0.0.0.0' ,port= 8080 ,debug=True)

