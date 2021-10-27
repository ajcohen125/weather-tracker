from datetime import datetime

#Assuming logging file is open for all functions

#Custom event logging
def log_event(log_file, message, error_type):
    log_file.write("{0}[{1}] {2}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), error_type, message))

#Basic Logging
def log_error(log_file, message):
    log_file.write("{0}[ERROR] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_warning(log_file, message):
    log_file.write("{0}[WARNING] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_info(log_file, message):
    log_file.write("{0}[INFO] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

def log_debug(log_file, message):
    log_file.write("{0}[DEBUG] {1}\n".format((datetime.now().strftime("[%m-%d-%Y][%H:%M:%S]")), message))

