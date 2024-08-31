# delete the first node in the singly linked list
class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.head = None
        self.tail = None
        self.count = 0
        
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
            
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def del_first_item(self):
        if self.head == None:
            return None
        current = self.head
        self.head = self.head.next
        current.next = None
        self.count -= 1
        return current.data

#Driver code
footy_squads = singly_linked_list()
footy_squads.append_item("Tottenham Hotspur")
footy_squads.append_item("Roma")
footy_squads.append_item("BvB")
footy_squads.append_item("Lille")
footy_squads.del_first_item()
for club in footy_squads.iterate_item():
    print(club)
