#!/usr/bin/env python3
# Test python client to exercise
import dstc
from dstc import current_milli_time

def complex_arg(func_name, name, dynamic, age_array ):
    print("Function name: {}".format(func_name))
    print("Name: {}".format(name))
    print("Dynamic: {} / {}".format(dynamic, len(dynamic)))
    print("Age array: {}".format(age_array))

# PythonBinaryOp class is defined and derived from C++ class BinaryOp

if __name__ == "__main__":
    dstc.register_server_function("complex_arg",
                                  complex_arg,
                                  "32s#3i")
    dstc.activate()
    
    stop_ts = current_milli_time() + 400
    while (current_milli_time() < stop_ts):
            dstc.process_events(stop_ts - current_milli_time())

    dstc.process_pending_events()

