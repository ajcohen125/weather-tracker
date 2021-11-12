#!/usr/bin/env python3.9

import mysql.connector
import db
import sys
import getopt

config = {
  'user': 'temp',
  'password': 'Password1!',
  'host': '192.168.1.222',
  'database': 'temp',
  'raise_on_warnings': True
}

def main():
    print("I'm in the main")
    cnx = db.openConnection(user_name=config['user'], passwd=config['password'], host_ip=config['host'], db=config['database'])

    db.writeToDatabase(cnx)

    db.readDatabase(cnx)

    db.closeConnection(cnx)


main()