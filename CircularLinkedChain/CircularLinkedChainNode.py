class CircularLinkedChainNode:
    def __init__(self, key, item):
        self._key = key
        self._item = item

        self._next = None

    def getKey(self):
        return self._key

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setKeyAndItem(self, key, item):
        self._key = key
        self._item = item

    def setNext(self, next):
        self._next = next
