import numpy as np

class BaseQueue:
    def __init__(self, capacity, dtype=np.dtype('O')):
        self._values = np.zeros(capacity, dtype=dtype)
        self._capacity = capacity
        self._front = 0
        self._back = -1
    
    def is_empty(self):
        return self._front > self._back
    
    def _is_full(self):
        return self._back+1 >= self._capacity and self._front == 0
    
    def _reset_pos(self):
        pass
    
    def enqueue(self, value):
        if self._is_full():
            raise IndexError("enqueue to full queue")

        elif self.is_empty():
            self._front = 0
            self._back = 0
        else:
            self._back += 1
            if self._back >= self._capacity:
                self._reset_pos()
        self._values[self._back] = value
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._values[self._front]
        self._front += 1
        if self._front >= self._capacity:
            self._reset_pos()
        return value
    
    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        else:
            return self._values[self._front]
    
    def print_debug(self):
        for i in range(self._front, self._back + 1):
            i %= self._capacity
            print(self._values[i], end=' ')
        print()

class LinearQueue(BaseQueue):
    def _reset_pos(self):
        shift = self._front
        for i in range(self._front, self._back):
            self._values[i-shift] = self._values[i]
        self._front = 0
        self._back -= shift

class CircularQueue(BaseQueue):
    def __init__(self, capacity, dtype=np.dtype('O')):
        super().__init__(capacity, dtype=dtype)
        self._count = 0
    
    def is_empty(self):
        return self._count == 0
    
    def is_full(self):
        return self._count == self._capacity
    
    def _reset_pos(self):
        self._front %= self._capacity
        self._back %= self._capacity
    
    def enqueue(self, value):
        super().enqueue(value)
        self._count += 1
    
    def dequeue(self):
        value = super().dequeue()
        self._count -= 1
        return value