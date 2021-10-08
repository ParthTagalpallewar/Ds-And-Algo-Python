class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        strData = ""
        while(temp):
            strData += str(temp.data)+ ' --> ' if(temp.next) else str(temp.data)
            temp = temp.next
        print(strData)
 
    def insetAtEnd(self, data):
        if(self.head == None):
            self.head = Node(data, None)
        else:
            list = self.head
            while list.next:
                list = list.next
            node = Node(data, None)
            list.next = node

    def insetElements(self, list):
        for i in list:
            self.insetAtEnd(i)

    def insertSpecialNode(self, list):
        
        while list.next:
            list = list.next
        list.next = self.head

    def length(self, list):
        counter = 0

        head = list
        while head:
            counter += 1;
            head = head.next

        return counter

    def findIntersection(self, l1, l2):

        l1_size = self.length(l1)
        l2_size = self.length(l2)
      
        if(l1_size > l2_size):
             #l1 is greater
            i = l1_size - l2_size
                
            for _ in range(i):
                l1 = l1.next

        if(l1_size < l2_size):
            i = l2_size - l1_size
                
            for _ in range(i):
                l2 = l2.next

        while l1:
            if l1 == l2:
                return l1.data
            else:
                l1 = l1.next
                l2 = l2.next
        else:
            print("Not found")

   

if __name__ == "__main__":

    cl = LinkedList()
    cl.insetElements([9, 4, 5])

    l1 = LinkedList()
    l1.insetElements([1, 2, ])
    
    l2 = LinkedList()
    l2.insetElements([8, 9])
 
    cl.insertSpecialNode(l1.head)
    cl.insertSpecialNode(l2.head)

    l1.print()
    l2.print()

    intersectionPoint =  l1.findIntersection(l1.head, l2.head)
    print(intersectionPoint)


    
    
    