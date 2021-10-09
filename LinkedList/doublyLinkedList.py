class Node:
    
    def __init__(self,data,prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        head = self.head

        if(head is None):
            print("null")
            return 
        string = ""
        while head :
            string += str(head.data) + " ==> "
            head = head.next
        print(string)

    def reverse(self):

        head = self.head

        # if LL contain one node return linked head
        if head.next is None:
            return head

        while head:
            if(head.next is None):
                self.head = head
            head.prev, head.next = head.next, head.prev #interchaning head prev with next
            head = head.prev # moving head to next node

    # temp = head

    # # if LL contain one node return linked head
    # if head.next is None:
    #     return head

    # while head:
    #     if(head.next is None):
    #         temp = head
    #     head.prev, head.next = head.next, head.prev #interchaning head prev with next
    #     head = head.prev # moving head to next node
        
        
    # return temp 
    
    

            
   
    def insertAtEnd(self, data):
        head = self.head

        # if LL have no node return new Node
        if head is None:
            self.head =  Node(data)
            return

        # Move head to last node
        while head.next:
            head = head.next
       
        # insert new node at last
        head.next = Node(data, head, None)

    def insertElements(self, list):
        
        for element in list:
            self.insertAtEnd(element)


if __name__ == '__main__':
    
    list = DoublyLinkedList()

    list.insertElements([1, 2, 3, 4])
    list.reverse()
    list.print()
    