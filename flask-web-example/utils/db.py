import mysql.connector

config = {
    "host": "localhost",
    "user": "admin",
    "password": "administrador",
    "database": "learning"
}

db = mysql.connector.connect(**config)