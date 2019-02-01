class SLLNode:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __repr__(self):
        return f'SLLNode<{self.value}>'


class SingleLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def first(self):
        return self.start.value

    def last(self):
        return self.end.value

    def dump(self, arg):
        next_node = self.start
        while next_node:
            print(next_node)
            next_node = next_node.child

    def push(self, value):
        node = SLLNode(value)

        if not self.start:
            self.start = self.end = node
            return self

        self.end.child = node
        self.end = node

        return self

    def pop(self):
        if not self.start:
            return None

        if self.start == self.end:
            ret = self.start
            self.start = self.end = None
            return ret.value

        next_node = self.start
        while next_node.child != self.end:
            next_node = next_node.child

        ret = self.end
        self.end = next_node
        self.end.child = None
        return ret.value

    def shift(self, value):
        node = SLLNode(value, self.start)
        self.start = node
        if not self.end:
            self.end = node
        return node.value

    def unshift(self):
        if self.start is None:
            return None

        ret = self.start
        self.start = ret.child
        return ret.value

    def remove(self, value):
        n = 0
        next_node = self.start
        if next_node.value == value:
            self.start = next_node.child
            return n

        while next_node.value is not None:
            if next_node.child.value == value:
                next_node.child = next_node.child.child
                return n + 1
            next_node = next_node.child
            n += 1

    def count(self):
        n = 0
        next_node = self.start
        while next_node is not None:
            next_node = next_node.child
            n += 1
        return n

    def get(self, n):
        if not self.start:
            return None

        next_node = self.start
        for i in range(n):
            if next_node.child:
                next_node = next_node.child
            else:
                return None
        return next_node.value

