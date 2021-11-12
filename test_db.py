#!/usr/bin/env python3.9

import mysql.connector
import db
import sys

config = {
  'user': 'temp',
  'password': 'Password1!',
  'host': '192.168.1.222',
  'database': 'temp',
  'raise_on_warnings': True
}

def test_openConnection():
    cnx = db.openConnection(user_name=config['user'], passwd=config['password'], host_ip=config['host'], db=config['database'])
    return cnx

def test_writeToDB(cnx):
    db.writeToDatabase(cnx)

def test_readDB(cnx):
    db.readDatabase(cnx)

def test_closeConnection(cnx):
    db.closeConnection(cnx)

