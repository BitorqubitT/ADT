from CircularLinkedChainNode import CircularLinkedChainNode


class CircularLinkedChain:
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

        node = CircularLinkedChainNode(key, item)

        if self._size == 0:
            node.setNext(node)
            self._head = node
        elif index == 0:
            node.setNext(self._head)

            last_node = self._head
            for i in range(self._size+1):
                last_node = last_node.getNext()

            last_node.setNext(node)

            self._head = node
        else:
            prev_node = self._head
            for i in range(index-1):
                prev_node = prev_node.getNext()

            next_node = prev_node.getNext()
            prev_node.setNext(node)
            node.setNext(next_node)

        self._size += 1
        return True

    def delete(self, index):
        if index < 0 or index >= self._size or self._size == 0:
            raise ValueError("index is not valid")

        if self._size == 1:
            self._head = None
        elif index == 0:
            prev_node = self._head
            for i in range(self._size-1):
                prev_node = prev_node.getNext()

            self._head = self._head.getNext()
            prev_node.setNext(self._head)
        else:
            prev_node = self._head
            for i in range(index-1):
                prev_node = prev_node.getNext()

            node = prev_node.getNext()

            prev_node.setNext(node.getNext())

            if node is self._head:
                self._head = node.getNext()

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
