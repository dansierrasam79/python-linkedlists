# find size of linked list
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

#Driver code
footy_squads = singly_linked_list()
footy_squads.append_item("Tottenham Hotspur")
footy_squads.append_item("Roma")
footy_squads.append_item("BvB")
footy_squads.append_item("Lille")
print("Number of clubs: ", footy_squads.count)
