def is_iterable(obj):
    try:
        iter(obj)
        return True

    except TypeError:
        return False


class Queue:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

        def get_item(self):
            return self.item

        def get_next(self):
            return self.next

        def set_next(self, next):
            self.next = next

        def __repr__(self):
            return f"Queue Node: {repr(self.item)}"

    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0
        self.pointer = None

    def dequeue(self):
        if self.start == None:
            return None
        else:
            node = self.start
            self.start = node.get_next()
            self.length -= 1

            return node.get_item()

    def enqueue(self, item):
        node = self.end
        self.end = self.Node(item)

        if self.start == None:
            self.start = self.end
        else:
            node.set_next(self.end)

        self.length += 1


    def multi_enqueue(self, *items, suppress_warnings=False):
        if not suppress_warnings and len(items) <= 1:
            print("multi_enqueue should be used with more than 1 arguments")
        if len(items) == 1 and is_iterable(items[0]):
            items = items[0]
        for item in items:
            self.enqueue(item)


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.pointer == None:
            raise StopIteration
        else:
            node = self.pointer
            self.pointer = node.get_next()
            return node.get_item()

    def __len__(self):
        return self.length

    def __list__(self):
        return [i for i in self]

    def __repr__(self):
        return f"Queue {repr(list(self))}"

class Clock:
    def __init__(self, time=0):
        self.__time = time

    def tick(self):
        self.__time += 1

    def get_time(self):
        return self.__time

    def __repr__(self):
        return f"<Clock {self.get_time()}>"

class Event:
    def __init__(self, item):
        self.item = item

    def activate(self):
        pass

    def __repr__(self):
        return f"Event {self.item}"

class Events:
    def __init__(self, clock):
        self.clock = clock
        self.events = {}

    def schedule(self, event, time):
        if time not in self.events:
            self.events[time] = Queue()

        self.events[time].enqueue(event)

    def get_current_events(self):
        time = self.clock.get_time()

        if time in self.events:
            events = self.events[time]
        else:
            events = Queue()

        return events

    def activate_current_events(self):
        events = self.get_current_events()
        for event in events:
            event.activate()

    def __repr__(self):
        out = ""

        for event in sorted(list(self.events)):
            out += f"{event}: {self.events[event]}\n"
        return out[:-2]
