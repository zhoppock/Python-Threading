# borrowing the same code as seen in MultiThreading1.py
# here we simulate a Processing Payment program that sends confirmaton once done
import threading
import time
class my_thread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        print("Start " + self.name + "\n")
        threadLock.acquire() # locks the current thread to let the other finish first
        print_time(self.name, 1, self.counter)
        threadLock.release() # releases the current thread once the other thread is finished
        print("Exit " + self.name + "\n")

class my_thread2(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self): 
        print("Start " + self.name + "\n")
        threadLock.acquire() # check to see if any other thread is locked before continuing the current thread
        threadLock.release() # if this was not here, the current thread could never be unlocked
        print_time(self.name, 1, self.counter)
        print("Exit: " + self.name + "\n")

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s %s" % (threadName, time.ctime(time.time()), counter) + "\n")
        counter -= 1 

threadLock = threading.Lock()

thread1 = my_thread(1, "Payment", 5)
thread2 = my_thread2(2, "Sending Email", 10)
thread3 = my_thread2(2, "Loading Page", 3)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("Thank you, feel free to continue shopping")
