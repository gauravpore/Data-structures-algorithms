class Node:
    #node class to create a node
    def __init__ (self,data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self,data): #insertion of new node
        if self.data:
            if data < self.data: #checking left subtree
                if self.left is None:
                    self.left= Node(data)
                else:
                    self.left.insert(data)
            if data>self.data: #checking right subtree
                if self.right is None:
                    self.right = Node(data) #creating new node with data
                else:
                    self.right.insert(data)

def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left),height(root.right))

#creating tree
root = Node(10)
root.insert(2)
root.insert(4)
root.insert(3)
root.insert(5)

print (height(root))
