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
 
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insertAtStart(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        # if there is no elements in LL then inset at start
        if(self.head is None):
            self.head = Node(data)
            return

        # else inset at end
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = Node(data)
   
    def insertAt(self, index, data):
        if(index < 0 or index > self.length()):
             raise Exception("Invalid Index")

        if(index == 0):
            self.insertAtStart(data)
            return

        temp = self.head
        count = 0

        # interate till we get index-1
        while(count != index-1):
            count+=1
            temp = temp.next

        node = Node(data, temp.next)
        temp.next = node
        
    def removeAt(self, index):
        if(index < 0 or index > self.length()):
             raise Exception("Invalid Index")

        if index == 0:
            self.head == self.head.next
            return
        
        count = 0
        temp = self.head

        while(count != index-1):
            temp = temp.next
            count += 1

        temp.next = temp.next.next
    
    def deleteNFromEnd(self, n):

        dummy = Node(0, self.head)

        fast = dummy
        slow = dummy

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        self.head = dummy.next

    def findMid(self):
    
        s = self.head
        f = self.head

        while f.next.next:
            f = f.next.next
            s = s.next

        print(" Mid - ", s.data)

if __name__ == "__main__":

    
    print(0 % 2)
    list = LinkedList() #head is null

    for i in range(20, 0, -1):
        list.insertAtStart(i)

    list.print()

    list.findMid()