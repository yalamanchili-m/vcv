#contiguous
class ContiguousAllocation:
    def __init__(self, size):
        self.disk = [0]*size
    def allocate(self, name, start, length):
        if start+length > len(self.disk) or any(self.disk[start:start+length]):
            return False
        for i in range(start, start+length): self.disk[i]=1
        return True
    def display(self): print("Disk:", "".join(map(str,self.disk)))

c = ContiguousAllocation(20)
print("Contiguous:", c.allocate("F1",2,5)); c.display()

#linked
class LinkedAllocation:
    def __init__(self, size):
        self.disk = [0]*size
        self.link = {}  
        self.files = {}  
    def allocate(self, name, blocks):
        if any(self.disk[b] for b in blocks): return False
        for i,b in enumerate(blocks):
            self.disk[b]=1
            self.link[b] = blocks[i+1] if i+1<len(blocks) else None
        self.files[name]=blocks[0]
        return True
    def display(self):
        for f,s in self.files.items():
            out=[]; cur=s
            while cur is not None:
                out.append(str(cur)); cur=self.link[cur]
            print(f"{f}: {' -> '.join(out)} -> NULL")
        print("Disk:", "".join(map(str,self.disk)))

l = LinkedAllocation(20)
print("Linked:", l.allocate("A",[1,4,9,10]), l.allocate("B",[3,5,8])); l.display()

#indexed
class IndexedAllocation:
    def __init__(self, size):
        self.disk = [0]*size
        self.index = {}  # name -> (idx_block, data_blocks)
    def allocate(self, name, idx_block, data_blocks):
        blocks = [idx_block]+data_blocks
        if any(self.disk[b] for b in blocks): return False
        for b in blocks: self.disk[b]=1
        self.index[name] = (idx_block, data_blocks)
        return True
    def display(self):
        for f,(idx,db) in self.index.items():
            print(f"{f}: idx {idx} -> {db}")
        print("Disk:", "".join(map(str,self.disk)))

ix = IndexedAllocation(20)
print("Indexed:", ix.allocate("X",2,[4,6,8,10]), ix.allocate("Y",12,[13,15,17])); ix.display()
