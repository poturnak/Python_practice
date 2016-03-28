#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# ______________________ Threading module ______________________
# 1. Import threading module
# 2. Create thread object and pass it the function you want to execute in a thread
# 3. !!! pass the function without ()
# 4. Start a thread
# 5. if you need to pass arguments use args and kargs
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs = {'sep': ' & '})
# --if you want the main thread to wait until all the threads are terminated you can use join() mehtod
# thread_obj.join() - means wait until the threads are done
# if you have 100 threads, keep track of them by putting them in the list
# then if you want to wait while all threads are done, use for loop to go over all threads, and call join() on them
# ===================================================================================================

import threading, time
print('start of the program!')

def nap_time():
    time.sleep(3)
    print('Wake up!')

thread_obj = threading.Thread(target=nap_time)
thread_obj.start()

print('End of the program')

# pass print function to another thread
thread_obj1 = threading.Thread(target=print, args=['dog', 'cat'], kwargs={'sep': '_'})
thread_obj1.start()
