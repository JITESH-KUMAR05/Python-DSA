class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next =next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node

    def insert_begin(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            itr = self.head
            self.head = node
            node.next = itr


    def print(self):
        if self.head == None:
            print("List is empty")
        else:
            itr = self.head
            llst = ""
            # while itr:
            #     llst += str(itr.data) + "-->"
            #     itr = itr.next
        # print(llst)
            while itr.next:
                print(f"{itr.data} --> ", end="")
                itr = itr.next
            print(itr.data,end="")


            
if __name__ == '__main__':
    ll = Linked_List()
    ll.insert_end(20)
    ll.insert_end(24)
    ll.print()
    ll.insert_begin(15)
    ll.insert_begin(10)
    ll.print()