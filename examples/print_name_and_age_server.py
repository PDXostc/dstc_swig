#!/usr/bin/env python3
#
# Simple server example
#
import dstc
from dstc import current_milli_time

do_exit = False
def do_print_name_and_age(func_name, name, age):
    global do_exit
    print("Name: {}".format(name))
    print("Age: {}".format(age))
    do_exit = True

if __name__ == "__main__":
    dstc.register_server_function("print_name_and_age",
                                  do_print_name_and_age,
                                  "32si")

    dstc.activate()

    stop_ts = current_milli_time() + 400
    while (current_milli_time() < stop_ts):
            dstc.process_events(stop_ts - current_milli_time())

    while not do_exit:
        dstc.process_events(-1)
