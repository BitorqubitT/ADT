class ADTStackNode:
    def __init__(self, item, previous = None, next = None):
        self.item = item
        self.next = next
        self.previous = previous
