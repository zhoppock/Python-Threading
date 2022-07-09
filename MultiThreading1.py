import threading
import time
class my_thread(threading.Thread): # sub class of the threading class, inherits Thread
    def __init__(self, threadID, name, counter): # count down from a given number, construct a thread at first
        threading.Thread.__init__(self) # handles low level processing
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self): # needs to be called run to start a thread
        print("Start " + self.name + "\n")
        print_time(self.name, self.counter, 5) # each thread will count down from 5 to 0
        print("Exit " + self.name + "\n")

# it is possible to create multiple threading classes with different run attributes

def print_time(threadName, delay, counter):
    while counter: # counter is True until it is 0
        time.sleep(delay) # delay one thread by a certain time to let another run
        print("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n") # prints the thread name, time, and counter value
        counter -= 1 

# Create threads
thread1 = my_thread(1, "Thread 1", 1) # the thread will delay for 1 second
thread2 = my_thread(2, "Thread 2", 1.5) # the thread will delay for 1.5 seconds

# Start threads, each will count down to 0 simultaneously, when one thread is delayed the other runs for the delay time
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exit Main Thread")