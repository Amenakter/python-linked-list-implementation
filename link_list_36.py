 class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()
    

    def get_lenght(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1 
            current_node = current_node.next
        return count
 
    def insert_at(self, index, data):
        if index <0 or index >self.get_lenght():
            print("Invalid index!")
            return

        if index == 0:
            self. append_at_begining(data)
            return


        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                node =Node(data , current_node.next)
                current_node.next = node
                return
            current_node = current_node.next
            count +=1             

   
   

 
 
 