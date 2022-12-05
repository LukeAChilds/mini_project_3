from flask import Flask ,render_template, request
import sqlite3
import pandas as pd
#App DNS is https://myapp.luke1234.dynv6.net/


app = Flask(__name__)

@app.route('/',methods =['GET','POST'])
def home():
    return render_template('home.html',title='Home')

@app.route('/entry',methods =['GET','POST'])
def entry():
    return render_template('entry.html',title='Entry')

@app.route('/postform',methods =['GET','POST'])
def post():
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    code = request.form.get('code')
    print(name,description,price,code)
    if name == '' or code == '' or int(price) <= int(0) or description =='' :
        print('Invalid form')
        return render_template('entry.html',title='Entry')

    with sqlite3.connect("mydb.db") as con:
        con.execute('CREATE TABLE IF NOT EXISTS product (name TEXT NOT NULL, description TEXT NOT NULL, price INTEGER NOT NULL, code TEXT PRIMARY KEY)')
        con.commit()
        con.execute("INSERT INTO product (name,description,price,code) VALUES (:name,:description,:price,:code)",{"name":name,"description":description,"price":price,"code":code})
        df = pd.read_sql("SELECT * FROM product",con)
        print(df)
    return render_template('home.html',title='Home')

@app.route('/data',methods =['GET','POST'])
def data():
    selection = request.form.get('category')
    print(selection)
    with sqlite3.connect("mydb.db") as con:
        if selection =='none':
            df = pd.read_sql("SELECT * FROM product",con)
        elif selection =='viewname':
            df = pd.read_sql("SELECT name FROM product",con)
        elif selection =='viewdescription':
            df = pd.read_sql("SELECT description FROM product",con)
        elif selection =='viewprice':
            df = pd.read_sql("SELECT price FROM product",con)
        elif selection =='viewcode':
            df = pd.read_sql("SELECT code FROM product",con)
        else:
            df = pd.read_sql("SELECT * FROM product",con)
        return render_template('data.html',title='Data',data=df)
if __name__=="__main__":
    app.run(debug=True,port= 5000)