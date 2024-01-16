"""
Change the log levels from debug to info and back to study the difference in run time. 
"""

import logging
from datetime import datetime
from timeit import timeit

ITERATIONS = 100000

log = logging.getLogger("root")

log.setLevel(logging.DEBUG)      # Changed this from DEBUG to INFO
ch = logging.StreamHandler()
log.addHandler(ch)

class Employee:
    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number
    
    def __str__(self) -> str:
        # log.info("__str__ method called!")
        return f"Employee Name: {self.name}, Number: {self.number}"

def log_f_string():
    log.debug(f"Employee details {emp}")


def log_pct_fmt_string():
    log.debug("Employee details %s" % emp)


def log_str_fmt():
    log.debug("Employee details {}".format(emp))

def log_deferred_eval():
    log.debug("Employee details %s", emp)

emp = Employee('John', '001')

response = {}

log.info("\nUsing f-string message objects")
response['f-string'] = timeit(log_f_string, number=ITERATIONS)

log.info("\nUsing %-formatting message objects without deferred interpolation")
response['pct-formatting'] = timeit(log_pct_fmt_string, number=ITERATIONS)

log.info("\nUsing str.format message objects")
response['str.format'] = timeit(log_str_fmt, number=ITERATIONS)

log.info("\nUsing %-formatting message objects with deferred interpolation")
response['deferred interpolation'] = timeit(log_deferred_eval, number=ITERATIONS)

log.info(response)