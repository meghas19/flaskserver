from flask import Flask,request,render_template,flash,redirect,url_for,session,logging,jsonify
from flask_mysqldb import MySQL

from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
mysql=MySQL(app)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="digilocker"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
@app.route('/getadhar',methods=['GET'])
def home():
    session['login']=False
    try:
        data=request.get_json()
        username = data['username']
            
        print("comes here",username)
            
        cur=mysql.connection.cursor()
        result=cur.execute("select * from locker where adharno=%s",[username])
        data=cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if result>0:
            print(data)
            return jsonify(data),201
        
            
            
        else:
            error="Invalid format"
            return jsonify(error),201


    except:
        error="Invalid format"
        return jsonify(error),201




    
if __name__=='__main__':
    app.secret_key="secret2345"
    app.run(debug=True)