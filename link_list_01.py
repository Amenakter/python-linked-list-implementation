class Node:
    def __init__(self, Data="Head", Next = None):
        self.Data = Data
        self.Next = Next
class LinkList:

    def __init__(self):
        self.Head = Node()   

    def get_length(self):
        cnt = 0
        current_node = self.Head
        while current_node:
            cnt += 1
            current_node = current_node.Next

        return cnt    


    def print_link_list(self):
        if self.Head is None:
            print("Link list is Empty")
            return
        current_node = self.Head
        info_str = " "
        while current_node:
            info_str = info_str + str(current_node.Data) +'-->'
            current_node = current_node.Next
        print(info_str)     
                       

    def insert_at_begining(self, Data):
        node = Node(Data, self.Head.Next)
        self.Head.Next = node   

    def insert_at_end(self, data):

        current_node = self.Head
        while current_node.Next :
            current_node = current_node.Next  

        current_node.Next = Node(data, None) 


    def insert_at(self, index , data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return        

        if index == 0:
            self.insert_at_begining(data)
            return
            
        cnt = 0
        current_node = self.Head
        while current_node:
            if cnt == index -1:
                node = Node(data , current_node.Next)
                current_node.Next = node
                return
            current_node = current_node.Next
            cnt +=1





if __name__== '__main__':

    ll = LinkList()
    ll.insert_at_begining(2)
    ll.insert_at_begining(4)
    ll.insert_at_begining(5)
    ll.insert_at_begining(7)
    ll.print_link_list()
    ll.insert_at_end(10)
    ll.insert_at_end(10)
    ll.print_link_list()
    ll.insert_at(3, 8)
    ll.insert_at(4, 3)
    ll.print_link_list()