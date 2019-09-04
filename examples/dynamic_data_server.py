#!/usr/bin/env python3
# Test python client to exercise DSTC.
import dstc
from dstc import current_milli_time

do_exit = False

def do_dynamic_data(func, dyndata, int_list):
    global do_exit
    print("Got server call {}".format(func))
    print("  Dyndata: {}".format(dyndata))
    print("  Dyndata len: {}".format(len(dyndata)))
    print("  Intlist: {}".format(int_list))
    do_exit = True

# PythonBinaryOp class is defined and derived from C++ class BinaryOp
if __name__ == "__main__":
    dstc.register_server_function("test_dynamic_function",
                                  do_dynamic_data,
                                  "#4i")
    dstc.activate()

    stop_ts = current_milli_time() + 400
    while (current_milli_time() < stop_ts):
            dstc.process_events(stop_ts - current_milli_time())

    while not do_exit:
        dstc.process_events(-1)
