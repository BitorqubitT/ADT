class DoublyLinkedListNode:
    def __init__(self, searchKey, newItem):
        self.searchKey = searchKey
        self.data = self.searchKey, newItem
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # no need for tail as always the next pointer of last object will remain as none
        self.size = 0

    def insertNode(self, searchKey=None, newItem=None):
        node = DoublyLinkedListNode(searchKey, newItem)   # make new node
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        node.prev = self.head

    def searchList(self, searchKey):
        p = self.head
        while p is not None:
            if p.data is not None:
                if p.data[0] == searchKey:
                    return p.data, p
            if p.next is not None:
                p = p.next
            else:
                return False

    def deleteNode(self, searchKey):
        p = self.searchList(searchKey)
        if p is None:
            return False
        elif p is not False:
            p = self.searchList(searchKey)[1]
            if p.prev is not None and p != self.head:
                p.prev.next = p.next
            else:
                self.head = p.next
            if p.next is not None:
                p.next.prev = p.prev
            return True
        else:
            return False

    def getList(self):
        node = self.head
        i = []
        while node:
            if node.data is not None:
                i.append(node.data)
                node = node.next
        return i

    def get_top(self):
        return self.head

