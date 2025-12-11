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
import time
shared_counter = 0
def increment_counter():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1  
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(f"Final shared_counter value: {shared_counter}")
