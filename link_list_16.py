class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()

    def insert_at_beginig(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_at(self):
        if self.head is None:
            print("LInk list is empty")
            return

        current_node = self.head
        info = " "
        while current_node:
            info = info + str(current_node.next) + " --> "
            current_node = current_node.next      
        print(info)
        