#!/usr/bin/env python3.9

import requests
import sys
import custom_logging as log

def internet_connection():
    #FIXME - Figure out how to check internet connection
    return 0


def website_urls(links_dict, log_file):
    for key in links_dict:
        response = requests.get(links_dict[key])
        if response.status_code != 200:
            log.log_warning(log_file, "\"" + key + "\"" + " link is broken.")
    return 0



#FIXME - Commets on stuff that need to be fixed

#Make the following a different functions

#Internect connection
#Check to make sure I can connect to the internet by pinging google or something
#Use try-catch to make sure internet
#use both ping method and request (curl) method
#Retry 5 times in 30 (maybe make it where you can pass in num tries and time between tries)
#Return an error code and message if it doesn't work after those tries and exit in main
#If no problems, return good

