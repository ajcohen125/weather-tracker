#!/usr/bin/env python3.9


import custom_logging as log

def test_open_file():
    log.open_file()

def test_log_error():
    log.log_error("No internet connection - Console Print", True)
    log.log_error("No internet connection")

    log.log_warning("Link is broken - Console Print", True)
    log.log_warning("Link is broken")

    log.log_debug("No idea what this is for - Console Print", True)
    log.log_debug("No idea what this is for")
    
    log.log_info("task ran successfully - Console Print", True)
    log.log_info("task ran successfully")
    
    log.log_event("This is just a test - Console Print", "TEST", True)
    log.log_event("This is just a test", "TEST")

def test_close_file():
    log.close_file()

#Main
test_open_file()
test_log_error()
test_close_file()
