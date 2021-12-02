import time
from datetime import datetime


def consume_memory(gig: int, minutes: int):
    # Get current time
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    print("Current Time =", start_time)

    # Calc number of GB into bytes
    number_of_bytes = 1024000000 * gig

    # Calc minutes into seconds
    number_of_seconds = 60 * minutes

    # Use up memory in bytes
    temp_array = bytearray(number_of_bytes)

    # Sleep for number of seconds
    time.sleep(number_of_seconds)

    # Get current time
    now = datetime.now()
    end_time = now.strftime("%H:%M:%S")
    print("Current Time =", end_time)

    return_string = "Used " \
                    + str(gig) \
                    + "GB of memory for " \
                    + str(number_of_seconds) \
                    + " seconds. " \
                    + "Started at: " \
                    + str(start_time)  \
                    + ". Ended at:" \
                    + str(end_time)  \
                    + "."

    return return_string
