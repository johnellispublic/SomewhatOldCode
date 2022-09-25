from typing import Any, NewType, Iterable

def is_iterable(obj: Any):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True

class Queue(Iterable):
    #Allows for using Queue as a type in function declerations
    Queue = NewType('Queue', Any)

    class _Node:
        """A Node in a Queue

        It holds an item (of type any) for use in a Queue. The Queue is
        implemented in a linked list fashion.

        Attributes:
        |   Protected:
        |   |   _item (Any) - The item the Node holds
        |   |   _next (_Node) - The next item in the Queue (default: None)

        Methods:
        |   Magic:
        |   |   __init__(item: Any) - The constructor for _Node
        |
        |   Public:
        |   |   get_item() -> Any - Returns the item the Node holds
        |   |   set_next(new_next: Node) - Sets the next Node in the Queue
        |   |   get_next() -> _Node - Returns the next Node in the Queue
        """

        #Allows for using _Node as a type in function declerations
        _Node = NewType('_Node', Any)

        def __init__(item: Any):
            """The constructor for _Node

            Sets the _item attribute to what is specified and _next is None by
            default.

            arguments:
            |    item (Any) - The item the Node holds

            returns:
            |    None
            """
            self._item: Any
            self._next: _Node

            self._item = item
            self._next = None

        def get_item() -> Any:
            """Returns the item that the Node holds

            Arguments:
            |   None

            Returns:
            |   item (Any) - the item that the Node holds
            """
            return self._item

        def set_next(new_next: _Node) -> None:
            """Sets the next Node in the Queue

            This should be used when the Queue needs to either enqueue an item
            or remove an item in the middle (for whatever reason).

            Arguments:
            |    new_next (_Node) - The new node which follows this one

            Returns:
            |   None
            """
            if not isinstance(new_next, _Node):
                raise TypeError(f"{new_next} should be of type _Node, it is of \
                                  type {type(new_next)}")
            else:
                self._next = new_next

        def get_next() -> _Node:
            """Gets the next node in the Queue

            This should be used in the 'dequeue' method and for iterating
            through the queue

            Arguments:
            |   None

            Returns:
            |   next (_Node) - The next item in the Queue
            """
            return self._next

    def __init__(self):
        self._first: _Node
        self._last: _Node
        self._length: int
        self._pointer: int

        self._first = None
        self._last = None
        self._length = 0
        self._pointer = 0

    def is_empty(self) -> bool:
        if self._first is None:
            return True
        else:
            return False

    def enqueue(self, item: Any) -> None:
        new_node: _Node
        old_last: _Node

        new_node = _Node(item)
        old_last = self._last
        self._last = new_node

        if self.is_empty():
            self._first = new_node
        else:
            old_last.set_next(new_node)

        self._length += 1

    def dequeue(self) -> Any:
        old_first: _Node

        if self.is_empty():
            return None
        else:
            old_first = self._first
            self._first = first.get_next()
            self._length -= 1
            return old_first.get_item()

    def __len__(self):
        return self._length

    def __add__(self, other: Iterable) -> Queue:
        if not is_iterable(other):
            raise TypeError(f"{other} (type '{type(other)}') is not iterable")

        item: Any
        new_queue: Queue

        new_queue = Queue()
        for item in self:
            queue.enqueue(item)

        for item in other:
            queue.enqueue(item)

        return self
