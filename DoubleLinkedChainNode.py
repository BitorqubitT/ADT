class DoubleLinkedChainNode:
    def __init__(self, key, item):
        self._key = key
        self._item = item

        self._next = None
        self._prev = None

    def getKey(self):
        return self._key

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def getPrev(self):
        return self._prev

    def setKeyAndItem(self, key, item):
        self._key = key
        self._item = item

    def setNext(self, next):
        self._next = next

    def setPrev(self, prev):
        self._prev = prev
