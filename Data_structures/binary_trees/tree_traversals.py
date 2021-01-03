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



#Inorder traversal (Left->root->right)
def Inorder(root):
    #recursion
    if root:
        Inorder(root.left)
        print (root.data,end=" ")
        Inorder(root.right)

#root->left->right
def preorder(root):
    if root:
        print (root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

#left->right->root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def levelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue)>0:
        print (queue[0].data,end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)



root = Node(10)
root.insert(2)
root.insert(4)
root.insert(3)
root.insert(5)

print ("Inorder traversal:")
Inorder(root)

print("\nPreorder traversal:")
preorder(root)

print("\nPostorder traversal:")
postorder(root)

print("\nLevel order: ")
levelorder(root)

