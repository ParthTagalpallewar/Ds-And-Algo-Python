queue = []

def push(x):
    queue.append(x)

    for _ in range(len(queue)-1):
        queue.append(queue[0])
        queue.pop(0)
    
def pop():
    x = queue(0)
    queue.pop(0)
    return x

if __name__ == '__main__':
    
    push(1)
    push(2)
    push(3)
    print(queue)
    