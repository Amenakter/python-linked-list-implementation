class Node:
    def __init__(self, data = None , next= None) :
        self.data = data
        self.next = next

class LinkList:
    def __init__(self) :
        self.head = Node()

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
           node = Node(data , self.head.next)
           self.head.next = node
           return
            
        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index -1:
                node = Node(data , current_node.next)
                current_node.next = node
                return
            current_node = current_node.next
            cnt +=1

ll = LinkList()

print(ll.insert_at(1, 23)) 
print(ll.insert_at(2, 24)) 
print(ll.insert_at(3, 25)) 
print(ll.insert_at(4, 26)) 
 
 