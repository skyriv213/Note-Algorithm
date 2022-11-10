class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, val):
        idx = hash(key) % len(self.items)
        self.items[idx].add(key, val)

    def get(self, key):
        idx = hash(key) % len(self.items)

        return self.items[idx].get(key)
