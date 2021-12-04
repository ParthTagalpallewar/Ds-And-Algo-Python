def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("value added ", item)

def pop(stack):

    if check_empty(stack):
        print("Stack is Already Empty")
        return 
    
    return stack.pop()

if __name__ == '__main__':
    
    stack = create_stack()

    push(stack, 1)
    push(stack, 2)
    push(stack, 3)
    push(stack, 4)

    print(stack)

    print("Popped Item ", pop(stack))
    print(stack)
    
