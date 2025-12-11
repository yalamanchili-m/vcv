#fifo
def fifo_page_replacement(page_reference_string, num_frames):
    frames = []
    page_faults = 0
    for page in page_reference_string:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        print(f"Frames: {frames}")
    return page_faults

page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 3
page_faults = fifo_page_replacement(page_reference_string, num_frames)
print(f"Total page faults: {page_faults}")

#lru
from collections import deque
def lru_page_replacement(page_reference_string, num_frames):
    frames = []  
    page_faults = 0  
    access_order = deque()
    for page in page_reference_string:
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                lru_page = access_order.popleft()  
                frames.remove(lru_page)  
                frames.append(page) 
            page_faults += 1
        if page in access_order:
            access_order.remove(page)
        access_order.append(page)
        print(f"Frames: {frames}")
    return page_faults
page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 3
page_faults = lru_page_replacement(page_reference_string, num_frames)
print(f"Total page faults: {page_faults}")
