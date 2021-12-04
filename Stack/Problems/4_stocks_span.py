def calculateSpan(arr,n):
        st = []
        result = []
        
        st.append(0)
        result.append(1)
        
        for i in range(1, n):
            
            while len(st) > 0 and arr[st[-1]] <= arr[i]:
                st.pop()
                
            if len(st) == 0:
                result.append(i + 1)
            
            else:
                result.append(i - st[-1])
            
            st.append(i)
        return result

if __name__ == '__main__':
    
    prices = [100, 80, 60, 70, 60, 75, 85]
    
    a = calculateSpan(prices, len(prices))
    print(a)