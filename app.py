import mysql.connector
import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    return '<h1>Olá, CloudOpss Solutions!</h1>'


#Rotas para conectar ao banco de dados

@app.route('/funcionarios')
def get_funcionarios():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="testcloud",
    database="empresa"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM funcionarios")

  row_headers=[x[0] for x in cursor.cargo] #extrair os cabeçalhos das linhas

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="testcloud"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS empresa")
  cursor.execute("CREATE DATABASE empresa")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="testcloud",
    database="empresa"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS funcionarios")
  cursor.execute("CREATE TABLE funcionarios (nome VARCHAR(50), cargo VARCHAR(100))")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')