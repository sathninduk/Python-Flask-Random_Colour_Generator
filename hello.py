from flask import Flask
app = Flask(__name__)

import random
import mysql.connector

mydb = mysql.connector.connect (
    user = "root",
    password = "rootroot",
    host = "127.0.0.1",
    port = 3306,
    database = "python",
    raise_on_warnings = True
)
mycursor = mydb.cursor()
mycursor.execute("SELECT fname FROM users WHERE id=1")

myresult = mycursor.fetchall()
for x in myresult:
    @app.route('/')
    @app.route('/index')
    def index():
        return "Python on browser!" + str (x)







#import random
#print("rgb(" + str (random.randrange(0, 255)) + "," + str (random.randrange(0, 255)) + "," + str (random.randrange(0, 255)) + ")")

#if 1>2:
#    x = "True"
#else:
#    x = "False"
#print (type(x))

# comment
#i = 234.0 / 331
#k = i + 5
#a = k
#x, y, z = 1, 3, a
#print(x)
#print(y)
#print(z)

#cars = ["volvo", "toyota", "bmw"]
#x, y, z = cars
#print(x)
#print(x)
#print(z)

#x = 5.654
#print(int(x))

#x = int(3)
#print(complex(x))