import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'ugo',
    user = 'root',
    password  = ''
)

mycursor = mydb.cursor(dictionary=True)




mycursor.execute(
    """CREATE TABLE IF NOT EXISTS books(
        id INT NOT NULL AUTO_INCREMENT,
        bookname VARCHAR(100),
        author VARCHAR(100),
        dateofpublication VARCHAR(100),
        isbn VARCHAR(100),
        PRIMARY KEY(id)
    )
    """
)


