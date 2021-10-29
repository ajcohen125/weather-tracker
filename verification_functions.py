#!/usr/bin/env python3.9

import requests
import sys
#import custom_logging as log

def internet_connection():
    #FIXME - Figure out how to check internet connection
    return 0


def website_urls(links_dict, log_file, timeout_time = 1):

    for key in links_dict:
        try:
            response = requests.get(links_dict[key], timeout = timeout_time)
            
            if response.status_code % 100 != 2:
                response.raise_for_status()

        except requests.exceptions.Timeout as err:      #FIXME - replace print statments with log output for final version
            print("Timed out while attempting connection to \"{0}\" (Timeout = {1} sec)".format(key, timeout_time))
            continue

        except requests.exceptions.RequestException as err:
            if type(err) == requests.exceptions.HTTPError:
                print("\"{0}\" gave HTTP error code: {1}".format(key, response.status_code))
                continue

            elif type(err) == requests.exceptions.ConnectionError:
                print("Failed connection to \"{0}\"".format(key))
                continue

            else:
                print(err)
                continue

    return 0
                
                ### Next Steps ###
                #Make a good dict to return to the program and log each link as success under [INFO]
                #Log bad link errors to the log file and to the console with [WARNING]
                #Email us bad dict with broken links and  verification error type for each broken link (timeout, 404, etc)

                ### Other ###
                #Update log file to also print to console 
                #Look into ifdef type thing or optional argument for easy switchting between log and log/console


#FIXME - Commets on stuff that need to be implimented

#Internect connection
#Check to make sure I can connect to the internet by pinging google or something
#Use try-catch to make sure internet
#use both ping method and request (curl) method
#Retry 5 times in 30 (maybe make it where you can pass in num tries and time between tries)
#Return an error code and message if it doesn't work after those tries and exit in main
#If no problems, return good

