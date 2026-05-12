class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of the original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

l1=[34,23,45,56]
vals=['a','b','c','d']
myMap=Mapping(l1)
print(myMap.items_list)
mySubMap=MappingSubclass(l1)
mySubMap.update(keys=l1, values=vals)
print("SubClass:",mySubMap.items_list)