import re
from flask import Flask, render_template, request, redirect
from db import mydb, mycursor

app = Flask(__name__)


@app.route('/')
def author_list():
    return render_template('index2.html')



@app.route('/addbookpage')
def addbookpage():
    return render_template('addbooks.html')




@app.route('/addbook', methods = ['GET', 'POST'])
def addbook():
    bookname= request.form['bookname']
    author= request.form['author']
    date_of_publication= request.form['date']
    isbn = request.form['isbn']
    sql = ('INSERT INTO books (bookname,author, dateofpublication,isbn )VALUES (%s, %s, %s, %s)')
    values = (bookname,author,date_of_publication,isbn)
    mycursor.execute(sql, values)
    mydb.commit()
    return render_template('addbooks.html')



@app.route('/allbooks', methods = ['GET', 'POST'])
def allbooks():
    mycursor.execute('SELECT * FROM books')
    books = mycursor.fetchall()
    return render_template('allbooks.html', allbooks = books)



if __name__ == '__main__':
    app.run(debug=True)






