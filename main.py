#!/usr/bin/env python3.9

import mysql.connector
import db
import sys
import getopt

def main():
    print("I'm in the main")
    cnx = db.openConnection()

    db.readDatabase(cnx)

    db.closeConnection(cnx)


main()