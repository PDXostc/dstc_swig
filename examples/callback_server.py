#!/usr/bin/env python3
#
# Simple callback example - Server
#
import dstc
from dstc import current_milli_time

do_exit = False
def double_value_and_invoke_callback(func_name, value, callback):
    global do_exit
    print("Will double value: {}".format(value))
    # Invoke the callback in order to deliver the result.
    # The parameter signature ("i") specifies that an integer
    # is the single argument to be delivered.
    # This parametere signature must match the provided by
    # the remote client (such as callback_client.py) side invoking
    # this callback.
    callback("i", value * 2)
    do_exit = True

# PythonBinaryOp class is defined and derived from C++ class BinaryOp

if __name__ == "__main__":
    dstc.register_server_function("double_value_server",
                                  double_value_and_invoke_callback,
                                  "i&")
    dstc.activate()

    stop_ts = current_milli_time() + 400
    while (current_milli_time() < stop_ts):
            dstc.process_events(stop_ts - current_milli_time())

    while not do_exit:
        dstc.process_events(-1)

    # Make sure we get the last packets out
    dstc.process_events(500)
