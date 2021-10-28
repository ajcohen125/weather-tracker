#!/usr/bin/evn python3.9

## Connections to mysql database 

import mysql.connector

config = {
  'user': 'temp',
  'password': 'Password1!',
  'host': '192.168.1.222',
  'database': 'temp',
  'raise_on_warnings': True
}

def readDatabase(cnx=mysql.connector):
    print("Reading from database")
    
    cursor = cnx.cursor()

    query =  ("SELECT name, owner, species FROM pet")
         
    cursor.execute(query)

    for (first_name, owner, species) in cursor:
        print(first_name + owner + species, sep=' ')

def writeToDatabase(cnx=mysql.connector):
    print("Writing to Databsase")

def openConnection():
    print("Opening connection to Database")

    cnx = mysql.connector.connect(**config)

    return cnx

def closeConnection(cnx=mysql.connector):
    print("Closing connection to Database")
    cnx.close()

