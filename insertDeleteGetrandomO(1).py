class RandomizedSet:

    def __init__(self):
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.elements:
            return False
        self.elements.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
