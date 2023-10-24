import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)



def load_jobs():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM jobs')
    result = cur.fetchall()
    cur.close()
    jobs = []
    for row in result:
        job = {
            'id': row[0],
            'title': row[1],
            'location': row[2],
            'salary': row[3]
        }
        jobs.append(job)
    return jobs

@app.route("/")
def hello():
    jobs = load_jobs()
    return render_template('home.html', jobs=jobs)
 

# here route is making problem i think i have to create route for the 
#apply.html seperately and when the submit is done i have to create a post 
# route for that route

@app.route("/apply.html/<int:job_id>", methods=["POST"])
def apply(job_id):
    if request.method == "POST":
        applicant_name = request.form["applicant_name"]
        applicant_email = request.form["applicant_email"]
        application_text = request.form["application_text"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO applications (job_id, applicant_name, applicant_email, application_text) VALUES (%s, %s, %s, %s)",
            (job_id, applicant_name, applicant_email, application_text)
        )
        mysql.connection.commit()
        cur.close()

        flash("Application submitted successfully", "success")   
        
    return redirect(url_for("hello"))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

 