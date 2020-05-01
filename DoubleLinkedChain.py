from DoubleLinkedChainNode import DoubleLinkedChainNode


class DoubleLinkedChain:
    def __init__(self):
        self._head = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def getLength(self):
        return self._size

    def insert(self, index, key, item):
        if index < 0 or key is None or index > self._size:
            raise ValueError("index is not valid")
        if key is None:
            raise ValueError("key is not valid")

        node = DoubleLinkedChainNode(key, item)

        if self._size == 0:
            node.setNext(node)
            node.setPrev(node)
            self._head = node
        elif self._size == index:
            node.setNext(self._head)
            node.setPrev(self._head.getPrev())

            node.getPrev().setNext(node)

            self._head.setPrev(node)
        elif index == 0:
            node.setNext(self._head)
            node.setPrev(self._head.getPrev())
            self._head.setPrev(node)

            if self._size == 1:
                self._head.setNext(node)

            self._head = node
        else:
            repl = self._head
            for i in range(index):
                repl = repl.getNext()

            node.setNext(repl)
            node.setPrev(repl.getPrev())

            repl.getPrev().setNext(node)
            repl.setPrev(node)

        self._size += 1
        return True

    def delete(self, index):
        if index < 0 or index >= self._size or self._size == 0:
            raise ValueError("index is not valid")

        if self._size == 1:
            self._head = None
        else:
            item = self._head
            for i in range(index):
                item = item.getNext()

            if item is self._head:
                self._head = item.getNext()

            item.getPrev().setNext(item.getNext())
            item.getNext().setPrev(item.getPrev())

        self._size -= 1
        return True

    def retrieve(self, index):
        if index < 0 or index >= self._size or self._size == 0:
            raise ValueError("index is not valid")

        item = self._head
        for i in range(index):
            item = item.getNext()

        return item.getItem()

    def sortAscending(self):  # bubblesort
        length = self.getLength()
        for i in range(length - 1, 0, -1):
            node = self._head
            for j in range(i):
                next_node = node.getNext()
                if node.getKey() > next_node.getKey():
                    node.setKeyAndItem(next_node.getKey(), next_node.getItem()), next_node.setKeyAndItem(node.getKey(), node.getItem())
                node = next_node

    def sortDescending(self):  # bubblesort
        length = self.getLength()
        for i in range(length - 1, 0, -1):
            node = self._head
            for j in range(i):
                next_node = node.getNext()
                if node.getKey() < next_node.getKey():
                    node.setKeyAndItem(next_node.getKey(), next_node.getItem()), next_node.setKeyAndItem(node.getKey(), node.getItem())
                node = next_node

    def __getitem__(self, item):
        return self.retrieve(item)

    def __iter__(self):
        self._gdx = -1
        return self

    def __next__(self):
        self._gdx += 1

        if self._gdx >= self._size:
            del self._gdx
            raise StopIteration

        return self.retrieve(self._gdx)
