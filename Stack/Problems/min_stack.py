class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return "Node({})".format(self.value)


class Stack:

    def __init__(self):
        self.top = None
        self.count = 0
        self.min = None
    
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))
         
     # This method is used to get minimum element of stack
    
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
     
    def isEmpty(self):
        return self.top == None
    
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count

      # This method returns top of stack    
    
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
 
    def push(self, value):
        #check if stack is empty
        if self.top == None:
            self.top = Node(value)
            self.minimum = value
        
        # if new minimum value found
        if value < self.minimum:
            temp = (2 * value) - self.minimum
            self.top = Node(temp, self.top)
            self.minimum = value
        
        else:
            self.top = Node(value, self.top)

        print("Number Inserted: {}" .format(value))

    def pop(self):

        #check if stack is empty
        if self.top == None:
            return "Stack is Empty"
        
        removedNode = self.top.value
        self.top = self.top.next
        if removedNode < self.minimum:
            print ("Top Most Element Removed :{} " .format(self.minimum))
            self.minimum = ( ( 2 * self.minimum ) - removedNode )
        else:
            print ("Top Most Element Removed : {}" .format(removedNode))