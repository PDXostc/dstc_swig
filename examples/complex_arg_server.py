#!/usr/bin/env python3
# Test python client to exercise
import dstc
from dstc import current_milli_time
do_exit = False

def complex_arg(func_name, name, dynamic, age_array ):
    global do_exit
    print("Function name: {}".format(func_name))
    print("Name: {}".format(name))
    print("Dynamic: {} / {}".format(dynamic, len(dynamic)))
    print("Age array: {}".format(age_array))
    do_exit = True


if __name__ == "__main__":
    dstc.register_server_function("complex_arg",
                                  complex_arg,
                                  "32s#3i")
    dstc.activate()

    stop_ts = current_milli_time() + 400
    while (current_milli_time() < stop_ts):
            dstc.process_events(stop_ts - current_milli_time())

    while not do_exit:
        dstc.process_events(-1)
