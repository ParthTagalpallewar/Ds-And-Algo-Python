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
        
    def insertElements(self, data):

        for _ in data:
            self.insertAtEnd(_)
        
    def getNthFromLast(self, position):
        dummy = Node(0, self.head)

        fast = dummy
        slow = dummy

        counter = 0
        while(fast and counter != position):
            fast = fast.next
            counter += 1

      
        while(fast.next):
            slow = slow.next
            fast = fast.next
            
        print(slow.data)

    # [1, 1, 2, 3] -> [2, 3]
    def removeAllDuplicates(self):

        #[0, 1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 6]

        prev = Node(None, self.head)
        
        head = prev # head = 0
    
        start = prev.next # start = #[1, 1, 1, 1, 2, 3, 4, 4, 4, 5, 6]
        selected = None

        while(start.next): # 1 -> 1
            if(start.data == start.next.data): # 1 == 1
                selected = start.data # selected = 1
                
                while(start.next and start.next.data == selected): 
                    start = start.next # start -> 1 position 4
                
                if(start.next): 
                    prev.next = start.next 
                    prev = start
                    start = start.next
                else:
                    prev.next = None
                    break

                
            else:
                prev = start
                start = prev.next
                
                
            
                
        self.head = head.next    

    def removeDuplicates(self):

        # 0 0 0 0 0 0 0
   
        prevNode = self.head
        nextNode = prevNode.next 

        while(nextNode):

            if(prevNode.data == nextNode.data):
                while(nextNode and prevNode.data == nextNode.data):
                        nextNode = nextNode.next 
                prevNode.next = nextNode
            else:
                prevNode = prevNode.next 
                nextNode = prevNode.next








if __name__ == "__main__":

    
    list = LinkedList() #head is null

    list.insertElements("12234")
    
    list.print()

    list.removeDuplicates()

    list.print()