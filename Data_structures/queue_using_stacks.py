#implementing queue using stacks
#method: enqueue costly

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,x):
        while len(self.stack1)!=0: #moving all the elements to stack2
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        self.stack1.append(x) #pushing new element x
        while len(self.stack2)!=0: #moving all elements again to stack1
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):
        if len(self.stack1)==0:
            print ("Empty")
        else:
            item = self.stack1.pop()
            return "removed element",item


queue1 = Queue()
queue1.enqueue(1)
queue1.enqueue(3)
queue1.enqueue(5)
print (queue1.dequeue())