#Represent a node of doubly linked list    
class Node:    
    def __init__(self,data):    
        self.data = data
        self.previous = None    
        self.next = None
            
class DoublyLinkedList:    
    #Represent the head and tail of the doubly linked list    
    def __init__(self):    
        self.head = None
        self.tail = None
        self.count = 0
            
    #addNode() will add a node to the list    
    def addNode(self, data):    
        #Create a new node    
        newNode = Node(data)    
            
        #If list is empty    
        if(self.head == None):    
            #Both head and tail will point to newNode    
            self.head = self.tail = newNode    
            #head's previous will point to None    
            self.head.previous = None
            #tail's next will point to None, as it is the last node of the list    
            self.tail.next = None
        else:    
            #newNode will be added after tail such that tail's next will point to newNode    
            self.tail.next = newNode
            #newNode's previous will point to tail    
            newNode.previous = self.tail
            #newNode will become new tail    
            self.tail = newNode
            #As it is last node, tail's next will point to None    
            self.tail.next = None
        self.count += 1

    def reversedll(self):
        """ Reverse linked list. """
        current = self.head
        while current:
            temp = current.next
            current.next = current.previous
            current.previous = temp
            current = current.previous
        temp = self.head
        self.head = self.tail
        self.tail = temp
    
    #display() will print out the nodes of the list    
    def display(self):    
        #Node current will point to head    
        current = self.head
        if(self.head == None):    
            print("List is empty")
            return;    
        print("Nodes of doubly linked list: ")

        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.data) 
            current = current.next;    
                
dList = DoublyLinkedList() 
#Add nodes to the list
for num in range(1,6):
    dList.addNode(num)

#Displays the nodes present in the list    
dList.display()

dList.reversedll()

#Displays the nodes in reverse order present in the list    
dList.display()
