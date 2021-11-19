def maxWays(n: int):

    if n == 1 or n == 2:
        return n

    a = 1
    b = 2

    for i in range(2, n):
        sum = a + b
        a = b
        b = sum
    
    return b

if __name__ == '__main__':
    
    n = maxWays(5)
    print(n)