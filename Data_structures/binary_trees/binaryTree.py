class Node:
    def __init__(self,data):
       self.data = data
       self.right = None
       self.left  = None

    def insert(self,data):
        if self.data:
            if data<self.data:
             if self.left is None:
                self.left = Node(data)
             else:
                self.left.insert(data)
            if data>self.data:
             if self.right is None:
                self.right = Node(data)
             else:
                self.right.insert(data)
        else:
            self.data = data

    def findval(self,val):
        if val<self.data:
            if self.left is None:
                return "Not Found in left"
            return self.left.findval(val)
        elif val>self.data:
            if self.right is None:
                return "Not Found in right"
            return self.right.findval(val)
        else:
            return ("Found")

            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print (self.data,end=" "),
        if self.right:
            self.right.printTree()

def printInorder(root):
        if root:
         printInorder(root.left)
         print (root.data)
         printInorder(root.right)

root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(6)



print(root.findval(5))




