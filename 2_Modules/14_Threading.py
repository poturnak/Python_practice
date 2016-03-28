#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# ______________________ Threading module ______________________
# 1. Import threatding module
# 2. Create thread object and pass it the function you want to execute in a thread
# 3. !!! pass the function without ()
# 4. Start a thread
# ===================================================================================================

import threading, time
print('start of the program!')

def nap_time():
    time.sleep(3)
    print('Wake up!')

thread_obj = threading.Thread(target=nap_time)
thread_obj.start()

print('End of the program')
