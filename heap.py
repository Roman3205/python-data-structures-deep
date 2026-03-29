class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    # O(log n)
    def insert(self, key, value):
        self.heap.append([key, value])
        self._sift_up(len(self.heap)-1)

    # O(1)
    def peek_min(self):
        if not self.heap:
            raise IndexError("Peek is empty")
        return self.heap(0)

    # O(log n)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Peek is empty")
        min_element = self.heap[0]
        last_element = self.heap.pop()

        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return min_element
    
    # O (n)
    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)):
            self._sift_down(i)

    # O (n)
    def meld(self, other_heap):
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

    # O (1)
    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None
    
    # O (n)
    def __iter__(self):
        for i in self.heap:
            yield i

    # O (1)
    def _left(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    # O (1)
    def _right(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    # O (log n)
    def _sift_up(self, index):
        parent_index = self._parent(index)
        
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    # O (log n)
    def _sift_down(self, index):
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break

            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            index = smallest

if __name__ == "__main__":
    heap = MinHeap()
    heap.heapify([[10, '10'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1']])
    print([k[0] for k in heap])

    import heapq
    my_l = [10,9,8,7,6,5,4,3,2,1]
    heapq.heapify(my_l)
    print(my_l)

    print(heap.extract_min())
    print(heap.extract_min())
    print(heapq.heappop(my_l))
    print(heapq.heappop(my_l))

    heap.insert(2, '2')
    print([k[0] for k in heap])

    heapq.heappush(my_l, 2)
    print(my_l)
