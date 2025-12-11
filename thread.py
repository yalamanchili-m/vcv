#program1
import threading
import time
def print_hello():
    for _ in range(5):  
        print("Hello")
        time.sleep(1) 
def print_world():
    for _ in range(5): 
        print("World")
        time.sleep(1)  
thread1 = threading.Thread(target=print_hello)
thread2 = threading.Thread(target=print_world)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished.")

#program2
import threading
count = 0
def inc():
    global count
    for _ in range(1000):
        count += 1
t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=inc)
t1.start()
t2.start()
t1.join()
t2.join()
print(count)
