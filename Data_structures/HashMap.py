#implementing Hash Table (Without using dict{})
class HashMap:
    def __init__(self,size):
        self.max_size = size
        self.arr = [None for i in range(self.max_size)]

    def gethash(self,key):
        h = 0
        for char in key:
            h+= ord(char) #getting ASCII values
        return h % self.max_size

    def insert(self,key,val):
        h = self.gethash(key)
        self.arr[h] = val

    def get(self,key):
        h = self.gethash(key)
        return self.arr[h]



h = HashMap(5)
h.insert("Jan",1)
h.insert("Oct",10)
h.insert("Dec",12)
print (h.get("Oct"))
print (h.get("Jan"))
