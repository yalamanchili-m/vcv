#pipes
from multiprocessing import Pipe, Process
def child_process(conn):
    message = conn.recv() 
    print(f"Child received message: {message}")
def parent_process(conn):
    message = "Hello from parent!"
    conn.send(message)  
    conn.close()
if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    child = Process(target=child_process, args=(child_conn,))
    child.start()
    parent_process(parent_conn)
    child.join()

#semaphores
from multiprocessing import Semaphore, Process
import time
def critical_section(sem, process_id):
    sem.acquire() 
    print(f"Process {process_id} entering critical section.")
    time.sleep(2) 
    print(f"Process {process_id} leaving critical section.")
    sem.release()  
if __name__ == "__main__":
    sem = Semaphore(1)  
    processes = []
    for i in range(5):
        p = Process(target=critical_section, args=(sem, i))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

#shared memory
import mmap
import os
import time
from multiprocessing import Process
def write_to_shared_memory(f):
    f.seek(0)
    f.write(b"Hello from writer process!")
    print("Writer process has written to shared memory.")
def read_from_shared_memory(f):
    time.sleep(1) 
    f.seek(0)
    content = f.read(100) 
    print(f"Reader process reads: {content.decode()}")
if __name__ == "__main__":
    filename = '/dev/shm/shared_mem_file' 
    size = 1024  
    with open(filename, 'w+b') as f:
        f.write(b'\x00' * size)
        f.flush()
        writer = Process(target=write_to_shared_memory, args=(f,))
        reader = Process(target=read_from_shared_memory, args=(f,))
        writer.start()
        reader.start()
        writer.join()
        reader.join()
    os.remove(filename)