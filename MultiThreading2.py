import threading
import time
class a_thread(threading.Thread): # sub class of the threading class, inherits Thread
    def __init__(self, threadID, name, counter): # count down from a given number, construct a thread at first
        threading.Thread.__init__(self) # handles low level processing
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self): # needs to be called run to start a thread
        print("Start " + self.name + "\n")
        print_time(self.name, 1, self.counter) # each thread will delay 1 second each
        print("Exit " + self.name + "\n")

# it is possible to create multiple threading classes with different run attributes

def print_time(threadName, delay, counter):
    count = 1
    while count < 1000: # loop goes until a thread's counter value is over 1000
        time.sleep(delay) # delay one thread by a certain time to let another run
        print("%s: %s %s" % (threadName, time.ctime(time.time()), count) + "\n") # prints the thread name, time, and counter value
        count *= counter

# Create threads
thread1 = a_thread(1, "Thread 1", 10) # the thread will count down from 10
thread2 = a_thread(2, "Thread 2", 5) # the thread will count down from 5
thread3 = a_thread(2, "Thread 3", 2) # the thread will count down from 5

# Start threads, each will count down to 0 simultaneously, when one thread is delayed the other runs for the delay time
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Exit Main Thread")