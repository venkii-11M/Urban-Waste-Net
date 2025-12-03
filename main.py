from flask import Flask , render_template
import mysql.connector 

app = Flask(__name__,template_folder='Website/templates',static_folder='Website/static')

mydb = mysql.connector.connect(host="localhost",user="Venkii",password="venkii@123")

mycursor =mydb.cursor()

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
   app.run(debug=True)