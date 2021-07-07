class Node:
    def __init__(self, data ="Head", next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = Node()

    def insert_at_begining(self , data):
        node = Node(data , self.head.next)
        self.head.next = node

    def print_at(self):
        if self.head is None:
            print("Link list is empty")
            return
        current_node = self.head
        info_str = " "
        while current_node:
            info_str = info_str + str(current_node.data) + "-->"
            current_node = current_node.next
        print(info_str)



    def insert_at_end(self, data):
        current_node =self.head 
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data, None)      

    
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt +=1
            current_node = current_node.next
        return cnt




    def insert_at(self, index , data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return


        if index == 0:
            self.insert_at_begining(data)
            return
        
        cnt= 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
               node = Node(data , current_node.next)
               current_node.next = node
               return
            current_node = current_node.next
            cnt +=1    




               
        
ll = LinkList()
ll.insert_at_begining(2)
ll.insert_at_begining(3)
ll.insert_at_begining(5)
ll.print_at()


ll.insert_at_end(1)
ll.insert_at_end(10)
ll.print_at()


ll.insert_at(4, 8)
ll.insert_at(3, 7)
ll.insert_at(8, 45)
ll.print_at()