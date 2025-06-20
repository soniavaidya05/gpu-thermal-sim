class PriorityQueue:
    def __init(self):
        self.heap = []
        self.size = 0

    def build_heap(self, items):
        self.heap = [None] + items  # Use 1-based indexing
        self.size = len(items)
        
        i = self.size // 2  # root
        
        while i > 0:
            self.bubble_down(i)
            i -= 1

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
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
            else:
                break   # nodes are in the right place 
    
    def bubble_up(self, i):
        # if the child's priority is less than its parent, swap them
        while i > 1 and self.heap[i].priority < self.heap[i // 2].priority:
            self._swap(i, i // 2)
            i = i // 2
    
    def push(self, item):
        self.heap.append(item)
        self.size += 1
        self.bubble_up(self.size)