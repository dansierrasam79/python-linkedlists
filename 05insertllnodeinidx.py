# insert node in a linkedlist based on index
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

    def insert_in_position(self,newVal,pos):
        newNode = Node(newVal)
        temp = self.head
        for i in range(2,pos):
            if temp.next != None:
                temp=temp.next
        newNode.next=temp.next
        temp.next=newNode

    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
            
#Driver code
items = singly_linked_list()
items_lst = ['PHP', 'Python', 'C#', 'C++', 'Java']
for item in items_lst:
    items.append_item(item)

# set the idx to position the element Rust in the linkedlst
lang_item = 'Rust'
lang_pos = 2

items.insert_in_position('Rust',lang_pos)

for lang in items.iterate_item():
    print(lang)
