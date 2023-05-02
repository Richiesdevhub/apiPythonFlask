from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'system'
mysql = MySQL(app)

@app.route('/customers') # GET
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, firstname, lastname, email, phone, address FROM customers")
    data = cur.fetchall()
    result = []
    for row in data:
        content = {
            'id': row[0], 
            'firstname': row[1], 
            'lastname': row[2], 
            'email': row[3], 
            'phone': row[4], 
            'address': row[5]
            }
        result.append(content)
    return jsonify(result)

@app.route('/customers/<int:id>') # GET
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT id, firstname, lastname, email, phone, address FROM customers WHERE id={str(id)}")
    data = cur.fetchall()
    content ={}
    for row in data:
        content = {
            'id': row[0], 
            'firstname': row[1], 
            'lastname': row[2], 
            'email': row[3], 
            'phone': row[4], 
            'address': row[5]
            }
    if content == {} :
        return "No se encuentra este cliente"
    else : 
        return jsonify(content)

@app.route('/customers', methods = ['POST']) # POST
def saveCustomer():
    #return request.json['firstname']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `customers` (`firstname`, `lastname`, `email`, `phone`, `address`) VALUES (%s, %s, %s, %s, %s);", (request.json['firstname'], request.json['lastname'], request.json['email'], request.json['phone'], request.json['address']))
    mysql.connection.commit()
    return 'Cliente guardado'

@app.route('/customers/<int:id>', methods = ['DELETE']) # DELETE
def removeCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE id="+str(id)+";")
    mysql.connection.commit()
    return "Cliente eliminado"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(None, 3000, True)