class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()

    def append_at_begining(self, data):
        node = Node(data , self.head.next)
        self.head.next = node

    def print_at(self):
        if self.head is None:
            print("link list is empty")
            return

        current_node = self.head
        info = " "
        while current_node:

            info = info + str(current_node.data) +" >> "
            current_node = current_node.next
        print(info)

ll = LinkList()
ll.print_at()
