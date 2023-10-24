import os
from flask import Flask, render_template 
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)


@app.route("/")
def load_jobs():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM jobs')
    jobs = cur.fetchall()   
    cur.close()
    return render_template('home.html', jobs=jobs)   



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

 