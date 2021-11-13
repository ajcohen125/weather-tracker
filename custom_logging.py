#!/usr/bin/env python3.9

from datetime import datetime

def open_file(file_name = "log.txt"):
    global log_file
    log_file = open(file_name,"a")
    log_info("Successfully opened log file")


def close_file():
    log_info("Closing log file")
    log_file.close()


#Custom event logging
def log_event(message, error_type, log_console = False):
    log_file.write("{0}[{1}] {2}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), error_type, message))
    if log_console:
        print("{0}[{1}] {2}".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), error_type, message))

#Basic Logging
def log_error(message, log_console = False):
    log_file.write("{0}[ERROR] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))
    if log_console:
        print("{0}[ERROR] {1}".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_warning(message, log_console = False):
    log_file.write("{0}[WARNING] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))
    if log_console:
        print("{0}[WARNING] {1}".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_info(message, log_console = False):
    log_file.write("{0}[INFO] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))
    if log_console:
        print("{0}[INFO] {1}".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_debug(message, log_console = False):
    log_file.write("{0}[DEBUG] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))
    if log_console:
        print("{0}[DEBUG] {1}".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

