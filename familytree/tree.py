import enum

class Gender(enum.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class Person:
    def __init__(self, gender, parents=[], children=[], age=0):
        self.parents = []
        self.children = []
        self.gender = gender
        self.age = age

    def add_child(self, child):
        assert self.age > child.age
        self.children.append(child)

    def add_parent(self, parent):
        assert self.age < parent.age
        self.parents.append(parent)

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age
