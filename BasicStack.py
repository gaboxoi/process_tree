class Stack:
    def __init__(self, list):
        self.items = list

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def to_list(self):
        temp = self.items.copy()
        temp.reverse()
        return temp