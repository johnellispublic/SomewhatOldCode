class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    # This method is a ">" operator. This means that you can compare two instances of Task eg
    # task1 = Task("a", 73)
    # task2 = Task("b", 21)
    # task1 > task2 will now return True as task1 > task2 is a just a shorthand for task1.__gt__(task2)
    def __gt__(self, other):
        return (self.priority > other.priority)

    # >= operator
    def __ge__(self, other):
        return (self.priority >= other.priority)

    # < operator
    def __lt__(self, other):
        return (self.priority < other.priority)

    # <= operator
    def __le__(self, other):
        return (self.priority <= other.priority)

    # Conversion to string, so what print(task1) returns
    def __str__(self):
        return "(" + str(self.name) + "," + str(self.priority) + ")"


class Heap:
    def __init__(self, capacity):
        # Note that index 0 is NOT used, numbers start from index 1 in a heap
        # This is to make calculations of parents/children simple - see below
        self.__items = [None] * (capacity + 1)
        # n is the number of items currently in the heap
        # Sounds like poor variable naming, but this is what it is normally called
        self.__n = 0
        self.__capacity = capacity

    def get_item_count(self):
        return self.__n

    def at(self, index):
        # Returns the value of an item at a given index
        if index < 1 or index > self.__n: return None
        return self.__items[index]

    def print_state(self):
        # Prints out items in the heap, level by level
        level_start = 1
        while level_start <= self.__n:
            for i in range(level_start, min(level_start*2, self.__n + 1)):
                print(self.at(i), end=" ")
            print("\n")
            level_start *= 2

    def is_empty(self):
        return (self.__n == 0)
    
    def is_full(self):
        return (self.__n == self.__capacity)

    def is_root(self, index):
        # Checks if an element at a given index is the root of the tree
        return (index == 1)
    
    def parent(self, index):
        # Returns index of the parent of an element with a given index
        # Check this formula on paper with a few examples!
        if self.is_root(index): return None
        return index // 2

    def left_child(self, index):
        # Returns index of left child of an element with a given index
        if index * 2 > self.__n: return None
        return index * 2

    def right_child(self, index):
        # Returns index of right child of an element with a given index
        if index * 2 >= self.__n: return None
        return index * 2 + 1
        
    def is_leaf(self, index):
        # Checks if an element is a leaf in the tree (ie has no children)
        # Check this formula with a few examples on paper and convince yourself it makes sense.
        return (self.left_child(index) is None)

    def __fix_upwards(self, index):
        # Your task is to follow this on paper using a few examples and figure out what it does
        if self.is_root(index): return
        parent = self.parent(index)
        if self.at(parent) < self.at(index):
            self.__items[parent], self.__items[index] = self.__items[index], self.__items[parent]
            self.__fix_upwards(parent)

    def __fix_downwards(self, index):
        # Your task is to follow this on paper using a few examples and figure out what it does
        if self.is_leaf(index): return
        largest_child = self.left_child(index)
        right_child = self.right_child(index)
        if right_child is not None and self.at(right_child) > self.at(largest_child):
            largest_child = right_child
        if self.at(largest_child) > self.at(index):
            self.__items[largest_child], self.__items[index] = self.__items[index], self.__items[largest_child]
            self.__fix_downwards(largest_child)

    def insert(self, value):
        # Inserts a value into the heap
        if self.is_full():
            raise IndexError('inserting into full heap')
        self.__n += 1
        index = self.__n
        self.__items[index] = Task(value, value)
        self.__fix_upwards(index)

    def top(self):
        # Returns the largest value in the heap
        if self.is_empty():
            raise IndexError('Seeing into an empty heap')
        return self.at(1).name

    def extract_max(self):
        # Returns the largest value in the heap and removes it from the heap
        if self.is_empty():
            raise IndexError('Extracting from an empty heap')
        value = self.at(1).name
        self.__items[1] = self.__items[self.__n]
        self.__n -= 1
        self.__fix_downwards(1)
        return value

n = int(input())
h = Heap(n)

for _ in range(n):
    command = input().split()
    if command[0] == 'insert':
        h.insert(int(command[1]))
    else:
        print(h.extract_max())
        

