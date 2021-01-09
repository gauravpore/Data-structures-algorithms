queue = []

def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print (element," is added to queue")

def dequeue():
    if not queue:
        print ("Empty")
    else:
        queue.remove(queue[0])
        print ("Element removed: ")

def display():
    print (queue)

while True:
    print ("Select the operation: 1.Add 2.Remove 3.Display 4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct option")

