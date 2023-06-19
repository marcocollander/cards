from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'raubuc.net'
app.config['MYSQL_USER'] = 'marcocollander'
app.config['MYSQL_PASSWORD'] = 'F@uq1935#xv$'
app.config['MYSQL_DB'] = 'marco_collander_1'

mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['signup-email']
        password = request.form['signup-password']
        cursor = mysql.connection.cursor()
        cursor.execute(
            'INSERT INTO threecards VALUES(%s,%s,%s,%s)',
            (id, name, email, password)
        )
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    
    return render_template('index.html')


# @app.route('/books', methods=['POST', 'GET'])
# def create_table():
#     if request.method == 'POST':
#         table = request.form['table']
#         cursor = mysql.connection.cursor()
#         query = f'CREATE TABLE {table}('\
#                 f'id INT NOT NULL PRIMARY KEY ,author VARCHAR(255), ' \
#                 f'title VARCHAR(255), edition VARCHAR(255), year VARCHAR(10))'
#         cursor.execute(query)
#         mysql.connection.commit()
#         cursor.close()
#         return f"Done!!"
#
#     return render_template('books.html')


if __name__ == '__main__':
    app.run(debug=True)
