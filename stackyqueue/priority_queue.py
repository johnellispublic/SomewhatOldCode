class PriorityQueue:
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__last = -1
        self.__count = 0
        self.__values = [0]*capacity
        self.__priorities = [0]*capacity
    
    def is_empty(self):
        return self.__count == 0
    
    def __is_full(self):
        return self.__count == self.__capacity
    
    def insert(self, value, priority):
        self.__last += 1
    
        if self.__is_full():
            raise IndexError('inserting into a full queue')

        self.__values[self.__last] = value
        self.__priorities[self.__last] = priority

        self.__count += 1
    
    def __find_max(self):
        max_priority = float('-inf')
        max_index = -1
        for index in range(0,self.__last+1):
            if self.__priorities[index] > max_priority:
                max_index = index
                max_priority = self.__priorities[index]
        
        return max_index

    def extract_max(self):
        if self.is_empty():
            raise IndexError('extracting from an empty queue')
        max_index = self.__find_max()
        value = self.__values[max_index]
        self.__values[max_index] = self.__values[self.__last]
        self.__priorities[max_index] = self.__priorities[self.__last]
        self.__count -= 1
        self.__last -= 1
        return value
    
    def top(self):
        if self.is_empty():
            raise IndexError('looking into an empty queue')
        max_index = self.__find_max()
        return self.__values[max_index]
    
    def print_debug(self):
        for i in range(0,self.__last+1):
            print(f"({self.__values[i]} priority {self.__priorities[i]})", end=' ')
        print()


n = int(input())
q = PriorityQueue(n)

for _ in range(n):
    command = input().split()
    if command[0] == 'insert':
        q.insert(int(command[1]),int(command[1]))
    else:
        print(q.extract_max())
