import mysql.connector

def conectar():
    database = mysql.connector.connect(
       host = "localhost",
       user = "root",
       password = "",
       database = "capp_citas",
       port = 3306
    )
    cursor = database.cursor(buffered = True)

    return [database, cursor]
