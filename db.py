#!/usr/bin/evn python3.9

## Connections to mysql database 

import mysql.connector
from mysql.connector import errorcode

def readDatabase(cnx=mysql.connector):
    print("Reading from database")
    
    cursor = cnx.cursor()

    query =  ("SELECT name, owner, species FROM pet")
         
    cursor.execute(query)

    for (first_name, owner, species) in cursor:
        print(first_name + owner + species, sep=' ')

def writeToDatabase(cnx=mysql.connector):
    print("Writing to Databsase")

def openConnection(user_name, passwd, host_ip, db):
    print("Opening connection to Database")
    
    try:
        cnx = mysql.connector.connect(user=user_name, password=passwd,
            host=host_ip, database=db)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return cnx

def closeConnection(cnx=mysql.connector):
    print("Closing connection to Database")
    cnx.close()

