class BaseStructure:
    class _Node:
        def __init__(self, item):
            self._item = item
            self._next = None

        def get_next(self):
            return self._next

        def set_next(self, next):
            if not isinstance(next, type(self)):
                raise TypeError( \
                    f"{next} should be of type _Node, not {type(next)}")
            else:
                self._next = next

        def get_item(self):
            return self._item

        def __repr__(self):
            return f"Node {repr(self._item)}"

    class _StructureIterator:
        def __init__(self, structure, return_node=False):
            if not isinstance(structure, BaseStructure):
                raise TypeError(f"{structure} should be a child of \
                                  {BaseStructure}")
            else:
                self._structure = structure
                self._pointer = structure.get_first()
                self._return_node = return_node

        def __iter__(self):
            return self

        def __next__(self):
            old_pointer = self._pointer
            if old_pointer is None:
                raise StopIteration


            self._pointer = self._pointer.get_next()
            if self._return_node:
                return old_pointer
            else:
                return old_pointer.get_item()

        def __repr__(self):
            return f"Iterator {repr(self.structure)}"

    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def __len__(self):
        return self._length

    def __iter__(self):
        iterator = self._StructureIterator(self)
        return iter(iterator)

    def is_empty(self):
        return self._first is None and self._last is None

    def get_first(self):
        return self._first
