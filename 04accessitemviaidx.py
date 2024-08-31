class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None
        self.count = 0
	
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
        return self.count

    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        pos = 0
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val,pos
            pos += 1

    def return_item(self,pos):
        current_item = self.head
        idx = 0
        while current_item:
            if idx == pos:
                val = current_item.data
                return [val,idx]
            current_item = current_item.next
            idx += 1

#Driver code
items = singly_linked_list()
items_lst = ['PHP', 'Python', 'C#', 'C++', 'Java']
for item in items_lst:
    items.append_item(item)

ll_idxs = [0,1,4,5,10]
for idx in ll_idxs:
    val_lst = items.return_item(idx)
    if val_lst:
        print(val_lst[0])
    else:
        print("Index out of range")
