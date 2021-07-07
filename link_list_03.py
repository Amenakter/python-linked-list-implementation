class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()

    def appent_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def print_at_begining(self):
        if self.head is None:
            print("Link List is empty!")
            return
        
        current_node = self.head
        info = " "
        while current_node:
            info = info + str(current_node.data) + " --> "
            current_node = current_node.next
            
        print(info)



    def append_at_end(self, data):
        current_node = self. head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data , None)


    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt +=1
            current_node = current_node.next
        return cnt

    def append_anyindex(self, index , data):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return
        
        if index == 0:
            self.appent_at_begining(data)
            return


        cnt = 0
        current_node = self.head
        while current_node.next:
            if cnt == index -1:
                node = Node(data, current_node.next)
                current_node.next = node
                return
            current_node = current_node.next
            cnt += 1     
        
ll = LinkList()

ll.print_at_begining()
ll.appent_at_begining(10)
ll.appent_at_begining(9)
ll.appent_at_begining(8)
ll.appent_at_begining(7)
ll.print_at_begining()


ll.append_at_end(45)
ll.append_at_end(48)
ll.append_at_end(50)
ll.print_at_begining()



ll.append_anyindex(2, 11)
ll.append_anyindex(4, 13)
ll.append_anyindex(5, 17)
ll.print_at_begining()

               

                
        