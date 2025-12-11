#contiguous
class ContiguousAllocation:
    def __init__(self, size):
        self.disk = [0] * size 
        self.size = size
    def allocate(self, filename, start, length):
        if start + length > self.size:
            print(f"Error: Not enough space to allocate {filename}")
            return
        if any(self.disk[start:start+length]):
            print(f"Error: Some blocks already allocated for {filename}")
            return
        for i in range(start, start + length):
            self.disk[i] = 1
        print(f"{filename} allocated from block {start} to {start + length - 1}")
    def display(self):
        print("Disk Status:", self.disk)
print("\n--- Contiguous Allocation ---")
contig = ContiguousAllocation(20)
contig.allocate("File1", 2, 5)
contig.allocate("File2", 8, 6)
contig.allocate("File3", 15, 4)
contig.display()

#linked
class LinkedAllocation:
    def __init__(self, size):
        self.disk = [0] * size
        self.links = {}  
        self.files = {}  
        self.size = size
    def allocate(self, filename, blocks):
        for b in blocks:
            if self.disk[b] == 1:
                print(f"Error: Block {b} already allocated.")
                return
        for b in blocks:
            self.disk[b] = 1
        for i in range(len(blocks) - 1):
            self.links[blocks[i]] = blocks[i + 1]
        self.links[blocks[-1]] = None 
        self.files[filename] = blocks[0]
        print(f"{filename} allocated at blocks: {blocks}")

    def display(self):
        for file, start in self.files.items():
            print(f"\nFile: {file}")
            current = start
            while current is not None:
                print(f"{current} -> ", end="")
                current = self.links[current]
            print("NULL")

        print("\nDisk Status:", self.disk)
print("\n--- Linked Allocation ---")
linked = LinkedAllocation(20)
linked.allocate("FileA", [1, 4, 9, 10])
linked.allocate("FileB", [3, 5, 8])
linked.display()

#indexed
class IndexedAllocation:
    def __init__(self, size):
        self.disk = [0] * size
        self.index_table = {}  
        self.size = size
    def allocate(self, filename, index_block, data_blocks):
        all_blocks = [index_block] + data_blocks
        for b in all_blocks:
            if self.disk[b] == 1:
                print(f"Error: Block {b} already allocated.")
                return
        for b in all_blocks:
            self.disk[b] = 1
        self.index_table[filename] = (index_block, data_blocks)
        print(f"{filename} allocated with index block {index_block} and data blocks {data_blocks}")
    def display(self):
        for file, (index, data) in self.index_table.items():
            print(f"\nFile: {file}")
            print(f"Index Block: {index} -> Data Blocks: {data}")
        print("\nDisk Status:", self.disk)
print("\n--- Indexed Allocation ---")
indexed = IndexedAllocation(20)
indexed.allocate("FileX", 2, [4, 6, 8, 10])
indexed.allocate("FileY", 12, [13, 15, 17])
indexed.display()
