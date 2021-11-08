def StocksSpan(price, n):

    st = [] # Decremental Order of Stocks
    result = [] # Span

    # adding idx of first element to stack
    st.append(0)

    # First Element in always 1
    result.append(1)

    for i in range(1, n):
        # st[-1] = 0, 
        # if 10 <= 4: false
        # if 
        
        while len(st) > 0 and price[st[-1]] <= price:
            st.pop()

        # len(st) -> 1
        if len(st) <= 0:
            result.append(i + 1)
        # 1 - 0 = 1
        # 2 - 0 = 2
        else:
            result.append(i - st[-1])

        st.append(i)


    return result

  

  
if __name__ == '__main__':
    
    price = [10, 4, 5, 90, 120, 80]
    N = len(price)

    stocksSpan = StocksSpan(price, N)
    print("Stocks Span are ", stocksSpan)
    