import numpy as np

def new_bool(value):
    if type(value) in [list, tuple,np.ndarray]:
        values = []
        for v in value:
            values.append(new_bool(v))
        return np.array(values,dtype=Bool)
    else:
        return Bool(value)

class Bool():
    def __init__(self, value):
        self.value = bool(value)

    def __and__(self, other):
        return Bool(self.value & bool(other))
    def __or__(self, other):
        return Bool(self.value | bool(other))
    def __xor__(self,other):
        return Bool(self.value ^ bool(other))
    def __invert__(self):
        return Bool(not self.value)

    def __eq__(self, other):
        return self.value == bool(other)

    def __add__(self, other):
        return Bool(self.value | bool(other))
    def __mul__(self, other):
        return Bool(self.value & bool(other))

    def __bool__(self):
        return self.value
    def __int__(self):
        return int(self.value)
    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return str(int(self))

def bin_table(var_num):
    table = np.ndarray((var_num,2**var_num))
    row = np.arange(2**var_num)
    for i in range(var_num):
        table[i] = row//2**(var_num-i-1)
        row %= 2**(var_num-i-1)

    return new_bool(table)
