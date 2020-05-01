from ADTStackNode import ADTStackNode

class ADTStack:
    def __init__(self):
        self._top = None
    def isEmpty(self):
        return self._top is None

    def push(self, value):
        newItem = ADTStackNode(value, None, self._top)

        if not self.isEmpty():
            self._top.previous = newItem
        
        self._top = newItem
        return True

    def pop(self):
        if self.isEmpty():
            return None, False

        old = self._top
        self._top = self._top.next

        if not self.isEmpty():
            self._top.previous = None

        return old.item, True

    def getTop(self):
        if self.isEmpty():
            return None, False
        else:
            return self._top.item, True
