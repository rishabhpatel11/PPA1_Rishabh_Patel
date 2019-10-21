from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import json
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'ppa2'
app.config['MYSQL_PORT'] = 3308
db = MySQL(app)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/bmi')
def displayBMITData():
   ip=request.remote_addr
   req=request.method + request.path
   cursor = db.connection.cursor()
   cursor.execute('''INSERT INTO web_requests(IP,request) VALUES (%s,%s)''',(ip,req))
   db.connection.commit()
   cursor.execute('''SELECT * FROM bmi_table''')
   attributes=[attribute[0] for attribute in cursor.description]
   query = cursor.fetchall()
   output=[]
   for q in query:
        output.append(dict(zip(attributes,q)))
   return json.dumps(output, indent=4, sort_keys=True, default=str)

@app.route('/distances')
def displayDistanceData():
   ip=request.remote_addr
   req=request.method + request.path
   cursor = db.connection.cursor()
   cursor.execute('''INSERT INTO web_requests(IP,request) VALUES (%s,%s)''',(ip,req))
   db.connection.commit()
   cursor.execute('''SELECT * FROM distances_table''')
   attributes=[attribute[0] for attribute in cursor.description]
   query = cursor.fetchall()
   output=[]
   for q in query:
        output.append(dict(zip(attributes,q)))
   return json.dumps(output, indent=4, sort_keys=True, default=str)

@app.errorhandler(500)
def internal_error(error):
    return "500 Error"

@app.errorhandler(404)
def not_found(error):
    return "404 Error"



if __name__ == '__main__':
   print("Go to http://localhost:5000/bmi or http://localhost:5000/distance to get json data")
   os.environ['WERKZEUG_RUN_MAIN'] = 'true'
   app.run(debug=False)
