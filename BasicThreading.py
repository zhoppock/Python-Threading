import threading #originally 'import thread' or 'import _thread' in Python2
import time

def func_thread():
    print('ran')
    time.sleep(1) #wait 1 second before going to the next line of code
    print("done")
    time.sleep(0.85)
    print("now done")

print("-----Threading Tutorial #1-----")
t1 = threading.Thread(target = func_thread)
t1.start() # program prints 'ran' first, then prints the threading active count, and finally prints "done"
print(threading.active_count()) # originally threading.activeCount()
time.sleep(1.2)
print("finally") # then the programs print "finally" and lastly prints "now done"


def counter1(n):
    for i in range(1, n + 1):
        print(i, end = " ")
        time.sleep(0.01)

def counter2(n):
    for i in range(1, n + 1):
        print(i, end = " ")
        time.sleep(0.02)

time.sleep(1) # prevents the previous tutorial's info from showing up here
print("\n-----Threading Tutorial #2-----")
for _ in range(2):
    t2 = threading.Thread(target = counter1, args = (10,)) # comma is needed to define a tuple (10, None), otherwise Python3 reads it as an integer value by itself
    t2.start()
print("Done")

time.sleep(1) # prevents the previous tutorial's info from showing up here
print("\n\n-----Threading Tutorial #3-----")
t3 = threading.Thread(target = counter1, args = (10,))
t3.start()
t4 = threading.Thread(target = counter2, args = (10,))
t4.start()
print("Done")

ls1 = [] # not the safest to use global memory when threading, just a heads up
ls2 = []
def counter3(n):
    for i in range(1, n + 1):
        ls1.append(i)
        time.sleep(0.5)

def counter4(n):
    for i in range(1, n + 1):
        ls2.append(i)
        time.sleep(0.5)

time.sleep(1) # prevents the previous tutorial's info from showing up here 
print("\n\n-----Threading Tutorial #4-----")
t5 = threading.Thread(target = counter3, args = (5,))
t5.start()
t6 = threading.Thread(target = counter3, args = (5,))
t6.start()
t5.join() # thread synchronization using the join method
t6.join() # the program does not go past these 2 lines of code until the function stops running
print(ls1)

t7 = threading.Thread(target = counter4, args = (5,))
t7.start()
t7.join() # once this thread is done, the next thread will begin
t8 = threading.Thread(target = counter4, args = (5,))
t8.start()
t8.join()
print(ls2)