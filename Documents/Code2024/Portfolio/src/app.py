from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Change if needed
app.config['MYSQL_DB'] = 'flask_users'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html', username=session.get('username'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password FROM tbl_users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[1], pwd):
            session['username'] = user[0]
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        
        hashed_pwd = generate_password_hash(pwd)
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_users (username, password) VALUES (%s, %s)", (username, hashed_pwd))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/feedback', methods=['POST'])
def feedback():
    username = request.form.get("username")
    email = request.form.get("email")
    message = request.form.get("msg")

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tbl_feedback (username, email, msg) VALUES (%s, %s, %s)", (username, email, message))
    
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

