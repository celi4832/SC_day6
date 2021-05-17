# Function in seperate fil to be included (using import) whenever you need it
# If any of the connection parameters change, you need to only change it one time

import mysql.connector # importere mysql connector

def dbconnect(): # definere connection til databasen
    connection = mysql.connector.connect( #login til databasen i mysql
        host="127.0.0.1",
        user="root",
        password="Kbq5nwo#",
        database="classicmodels"
    )
    return connection # returnere ens login til databasen
