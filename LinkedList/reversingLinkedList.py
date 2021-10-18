class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def print(self, listhead = None):
        temp = listhead if listhead is not None else self.head
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
    
    def middleElement(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle is ", slow.data)

    def reverse(self):
        saveNext = None
        current = self.head

        while current:
            next = current.next
            current.next = saveNext
            saveNext = current
            current = next
    
        self.head = saveNext

    def deleteNFromEnd(self, n):
        sizeOfList = self.length()
        current = self.head
        counter = 0 


        while (sizeOfList - counter) - 1 != n :

            print(sizeOfList, " ", counter, " ", n, " ", (sizeOfList - counter) - 1 )

            current = current.next
            counter += 1

        current.next = current.next.next

    def reverseInGroups(self, head, k):

            current = head
            next = None
            prev = None
            count = 0

            while current is not None and count < k:

                next = current.next
                current.next = prev
                prev = current
                current = next
                count += 1

            if next is not None:
                head.next = self.reverseInGroups(next, k)

            return prev

  
    


if __name__ == "__main__":

    
    list = LinkedList() #head is null

    list.insertElements([1, 2, 3, 4, 5, 6, 7, 8])

    list.print()
    
    head = list.reverseInGroups(list.head, 3)

    list.print(head)
