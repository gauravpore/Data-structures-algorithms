class Node:
    #func to create a node
    def __init__(self,data):
       self.data = data
       self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_front(self,data):
        #func to insert a new node at the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self,prev_node,data):
        new_node = Node(data)
        if prev_node is None:
            return
        new_node.next = prev_node.next
        prev_node.next = new_node


    def insert_end(self,data):
        #func to insert new node at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def printlist(self):
        #printing elemnts in Linkedlist
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

if __name__=='__main__':
 llist = Linkedlist()
 llist.insert_front(10)
 llist.insert_front(20)
 llist.insert_end(30)
 llist.insert_after(llist.head.next,25)
 llist.printlist()

