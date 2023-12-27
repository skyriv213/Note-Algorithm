class Bag:
    def __init__(self):
        self.bag = []

    def insert(self, stuff):
        self.bag.append(stuff)

    def remove(self, stuff):
        self.bag.remove(stuff)


my_bag = Bag()
my_bag.insert("사과")
print(my_bag.bag)
my_bag.remove("사과")
print(my_bag.bag)
