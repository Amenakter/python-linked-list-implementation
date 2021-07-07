


class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()
    
    def get_length(self):
        count = 0
        current_node = self.head
        while current_node.next:
            count += 1
            current_node = current_node.next
        return count    

    def print_at(self):
        if self.head is None:
            print("Link List is empty!")
            return
        
        current_node = self.head
        info = " "
        while current_node:
            info = info + str(current_node.data) + " --> "
            current_node = current_node.next
            
        print(info)

    def append_at_front(self, data):
        node = Node(data , self.head.next)
        self.head.next = node    



    def inser_at(self, index, data):
        if index < 0 or index > self.get_length():
            print("Inavlid index")
            return

        if index == 0:
            node = Node(data ,self.head.next)
            self.head.next = node
            return

        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                node = Node(data , current_node.next)
                current_node.next = node
                return
            current_node =current_node.next
            count += 1    
                         
 
ll= LinkList()


ll.append_at_front(23)
ll.append_at_front(23)
ll.append_at_front(23)
ll.append_at_front(23)
ll.inser_at(4, 20)
ll.inser_at(3, 20)
ll.print_at()
 