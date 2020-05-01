from ADTQueueNode import ADTQueueNode


class ADTQueue:
    def __init__(self):
        self._top = None

    def isEmpty(self):
        return self._top is None

    def enqueue(self, value):
        newItem = ADTQueueNode(value, None, self._top)

        if self.isEmpty():
            self._tail = newItem
        else:
            self._top.previous = newItem

        self._top = newItem
        return True

    def dequeue(self):
        if self.isEmpty():
            return None, False

        old = self._tail
        if self._tail == self._top:
            self._top = None
            self._tail = None
        else:
            self._tail.previous.next = None
            self._tail = self._tail.previous

        return old.item, True

    def getFront(self):
        if self.isEmpty():
            return None, False
        else:
            return self._tail.item, True
