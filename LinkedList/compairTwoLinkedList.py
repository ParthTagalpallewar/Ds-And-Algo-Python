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

    def mergeSortedList(self, l2):
        dummyNode = Node(0) # Creating Dummy Node
        dummyHead = dummyNode
        l1 = self.head 
        
        # Run while loop till one of list not get empty
        while l1 and l2:
            
            # compair l1 and l2 add smaller 
            # elements to dummynode

            if(l1.data > l2.data): 
                dummyNode.next = l2
                l2 = l2.next
                dummyNode = dummyNode.next
            else:
                dummyNode.next = l1
                l1 = l1.next
                dummyNode = dummyNode.next

        # add the remaining list to next of ended list
        if(l1 is None):
            dummyNode.next = l2
        
        if(l2 is None):
            dummyNode.next = l1

        # set the l1 to dummy none
        self.head = dummyHead.next

    def reversLinkList(self):
       
        previous = None
        li = self.head

        while(li):
            next = li.next
            li.next = previous
            previous = li
            li = next

        self.head = previous

    def compairTwoLinkedList(self, l1, l2):
        
        while(l1 and l2):
            if(l1.data != l2.data):
                return 0

            else:
                l1 = l1.next
                l2 = l2.next

        if(l1 or l2):
            return 0
        else:
            return 1

    def addLinkedlist(self, l1, l2):
        resultNode = Node(0)
        resulthead = resultNode
        
        carry = 0
        
        while l1 or l2:
            
            sum = carry

            if l1:
                sum += l1.data
                l1 = l1.next

            if l2:
                sum += l2.data
                l2 = l2.next
            
          
            carry = 0 if(sum < 10) else 1
            sum = sum % 10
           
            resultNode.next = Node(sum, None)
            resultNode = resultNode.next
            
        
            
        
            
        if carry == 1:
            resultNode.next = Node(carry, None)
           
            
            
            
        return resulthead.next

    def findMiddle(self):
        
        s = self.head
        f = self.head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        print(s.data)

    def checkPalindrome(self):

        head = self.head

        s = head
        f = head
        
        # go to middle of linked list
        while f and f.next:
            s = s.next
            f = f.next.next
            
        middle = s # finded middle
        
        #reverse the secound half part form middle
        
        previous = None
        
        while middle:
            print("reversing")
            next = middle.next
            middle.next = previous
            previous = middle
            middle = next
        
        reversedList = previous
        
        # head of seconnd half is at previous
        # check if list and previous is palindrome
        
        while reversedList and head:
            if head.data == reversedList.data:
                head = head.next
                reversedList = reversedList.next
            else:
                return False
        else:
            return True

        

if __name__ == "__main__":

    
    list1 = LinkedList() #head is null
   
    

    list1.insertElements([1, 2, 1])
   
  
    result = list1.checkPalindrome()

    print(result)

    
    

    