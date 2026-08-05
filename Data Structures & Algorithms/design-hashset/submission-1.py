class MyHashSet:

    def __init__(self):
        self.obj = [None] * 10000001
    def add(self, key: int) -> None:
        self.obj[key] = key

    def remove(self, key: int) -> None:
        self.obj[key] = None

    def contains(self, key: int) -> bool:
        return(self.obj[key] == key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)