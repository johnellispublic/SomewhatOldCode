import copy

class Terminal:
    def __init__(self, main):
        self.namespaces = {}
        self.base_namespace = main.__dict__

    def add(self, key):
        self.namespaces[key] = copy.copy(self.base_namespace)

    def restore(self, key):
        for item in list(self.base_namespace.keys()):
            if item not in self.namespaces[key] and item in self.base_namespace:
                del self.base_namespace[item]
        for item in self.namespaces[key]:
            self.base_namespace[item] = self.namespaces[key][item]
