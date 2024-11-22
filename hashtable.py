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
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        return 0
    def __getitem__(self, key):
        return self.arr[self.get_hash(key)]
    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None

# print(get_hash('march 6'))
ht = HashTable()
# print(ht.get_hash('march 6'))
# print((ht.add('march 6',130)))
# print(ht.arr)
# print(ht.get('march 6'))
# name changed for the functiona from add to setitem and get to getitem
ht['march 6'] = 130
ht['march 8'] = 30
print(ht['march 6'])
print(ht.arr)
del ht['march 6']
print(ht.arr)