"""Implements a stack"""

import numpy as np

class Stack:
    """Implements a stack

    Additional methods:
        __iter__   - iterate over it
        __len__    - the size of the stack
        __list__   - returns a list of the elements in the stack
        print_debug - prints the contents of the stack
    """
    def __init__(self, capacity, dtype=np.dtype('O')):
        self.__values = np.zeros(capacity, dtype=dtype) # The values in the stack
        self.__top = -1 # The index of the top of the stack
        self.__capacity = capacity # The capacity of the stack

    def push(self, value):
        """Standard push"""

        # Raise an error if it is full
        if self.__is_full():
            raise IndexError("push to full stack")

        # Otherwise append the value and increment top
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def pop(self):
        """Standard pop"""

        # Raise an error if it is empty
        if self.is_empty():
            raise IndexError("pop from empty stack")

        # Otherwise decrement top and return the value at what was the top
        else:
            self.__top -= 1
            return self.__values[self.__top+1]

    def peek(self):
        """Standard peek"""

        # Raise an error if the stack is empty
        if self.is_empty():
            raise IndexError("peek from empty stack")

        # Otherwise return the value at the top
        else:
            return self.__values[self.__top]

    def is_empty(self):
        """Standard is_empty"""
        return self.__top < 0

    def __is_full(self):
        """Checks if the stack is full"""
        return self.__top+1 >= self.__capacity

    def __iter__(self):
        """Iterates through the stack using a generator"""
        for i in range(0,self.__top+1):
            yield self.__values[i]

    def __len__(self):
        """Returns the number of elements in the stack"""
        return self.__top + 1

    def __list__(self):
        """Returns the list of the elements in the stack"""
        return list(self.__values[:len(self)])

    def print_debug(self):
        """Prints the contents in the stack"""
        print(' '.join(list(self)))
