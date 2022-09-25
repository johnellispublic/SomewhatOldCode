from base import BaseStructure

class Queue(BaseStructure):

    def enqueue(self, item):
        node = self._Node(item)
        if self.is_empty():
            self._first = node
            self._last = node

        else:
            old_last = self._last
            old_last.set_next(node)
            self._last = node

        self._length += 1

    def dequeue(self):
        if not self.is_empty():
            old_first = self._first
            self._first = old_first.get_next()
            self._length -= 1
            if self._first is None:
                self._last = None

            return old_first.get_item()
        else:
            return None
