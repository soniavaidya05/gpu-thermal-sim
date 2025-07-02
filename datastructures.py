class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def build_heap(self, items):
        self.heap = [None] + items  # Use 1-based indexing
        self.size = len(items)
        
        i = self.size // 2  # root
        
        while i > 0:
            self.bubble_down(i)
            i -= 1
    
    def is_empty(self):
        return self.size <= 0
    
    def __len__(self):
        return self.size
    
    def contains(self, item):
        return item in self.heap

    def bubble_down(self, i):
         while (i * 2) <= self.size:
            left = 2 * i
            right = 2 * i + 1

            # identify the smallest out of the subtree
            smallest = i
            if left <= self.size and self.heap[left].priority < self.heap[smallest].priority:
                smallest = left
            if right <= self.size and self.heap[right].priority < self.heap[smallest].priority:
                smallest = right

            # if a root's child smaller, switch root and child
            if smallest != i:
                self._swap(i, smallest)
            else:
                break   # nodes are in the right place 
    
    def bubble_up(self, i):
        # if the child's priority is less than its parent, swap them
        while i > 1 and self.heap[i].priority < self.heap[i // 2].priority:
            self._swap(i, i // 2)
            i = i // 2
    
    def push(self, item):
        if len(self.heap) != 0:
            self.heap.append(item)
            self.size += 1
            self.bubble_up(self.size)
        else:
            self.build_heap([item])
    
    def pop(self):
        if self.is_empty:
            return None  

        self._swap(1, self.size)
        min_job = self.heap.pop()  # remove last (formerly root)
        self.size -= 1
        self.bubble_down(1)
        return min_job
    
    def remove_by_id(self, job_id):
        for i in range(1, self.size + 1):
            if self.heap[i].id == job_id:
                return self.remove(i)
        return None  # Job not found

    def remove(self, i):
        if i > self.size or i <= 0:
            raise IndexError("Index out of bounds")

        self._swap(i, self.size)
        removed = self.heap.pop()
        self.size -= 1

        # Re-heapify at index i
        if i <= self.size:
            self.bubble_up(i)
            self.bubble_down(i)

        return removed

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_root(self):
        if not self.is_empty:
            return self.heap[1] 
        else:
            return None
    

    