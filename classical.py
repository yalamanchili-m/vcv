# dining_philosophers.py
import threading, time, random

N = 5
forks = [threading.Lock() for _ in range(N)]
room = threading.Semaphore(N - 1)  

def philosopher(id, rounds=3):
    left, right = id, (id + 1) % N
    for _ in range(rounds):
        print(f"Ph{id} thinking")
        time.sleep(random()*0.5)
        room.acquire()                
        with forks[left]:
            with forks[right]:
                print(f"Ph{id} eating")
                time.sleep(random()*0.3)
        room.release()
    print(f"Ph{id} done")

threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(N)]
for t in threads: t.start()
for t in threads: t.join()
print("All philosophers finished.")

# producer_consumer.py
import threading, queue, time, random

Q = queue.Queue(maxsize=5)
N_PRODUCE = 20
N_CONSUMERS = 2

def producer():
    for i in range(N_PRODUCE):
        Q.put(i)
        print(f"P produced {i}")
        time.sleep(random()*0.1)
    for _ in range(N_CONSUMERS):  
        Q.put(None)
        
def consumer(id):
    while True:
        item = Q.get()
        if item is None:
            Q.task_done()
            break
        print(f"C{id} consumed {item}")
        time.sleep(random()*0.2)
        Q.task_done()
    print(f"C{id} exiting")

threads = [threading.Thread(target=consumer, args=(i,)) for i in range(N_CONSUMERS)]
for t in threads: t.start()
prod = threading.Thread(target=producer)
prod.start()
prod.join()
Q.join()           
for t in threads: t.join()
print("All done.")
