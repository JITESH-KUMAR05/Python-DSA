# hash table implementation
class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for x in range(self.max)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
        return 0
    def get(self,key):
        return self.arr[self.get_hash(key)]

# print(get_hash('march 6'))
ht = HashTable()
# print(ht.get_hash('march 6'))
print((ht.add('march 6',130)))
# print(ht.arr)
print(ht.get('march 6'))