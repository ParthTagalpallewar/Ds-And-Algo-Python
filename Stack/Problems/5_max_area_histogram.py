def getMaxArea(histogram):
        
        histLen = len(histogram)
        
        RL = [0 for i in range(histLen)]
        LL = [0 for i in range(histLen)]
        
        stack = [] # stack will keep track of shortest element

        # add last element in stack
        stack.append(histLen-1)
        # As there is no right element at last element limit should be len of histogram
        RL[histLen-1] = histLen
        # count will keep track of peek element of stack
        count = 0
        
        # Iteration form last-second element of histogram 
        for i in range(histLen-2, -1, -1):
            # At first last element of histogram is present in stack
            # pop the peek element till it is greater than current so we get shortest element
            while count != -1 and histogram[i] <= histogram[stack[count]]:
                stack.pop()
                count -= 1
            # if stack is empty then there is no shorter element at right side so histlen is limit
            if count == -1:
                RL[i] = histLen
            # else assign limit of element as index of first shorter element at right
            else:
                RL[i] = stack[count]
            
            # at append stortest element in stack
            stack.append(i)
            count += 1

        # clear the stack so that it can be use to find left limits         
        stack.clear()

        stack.append(0)
        LL[0] = -1
        count = 0
        
        for i in range(1, histLen):
        
            while count != -1 and histogram[i] <= histogram[stack[count]]:
                stack.pop()
                count -= 1
            
            if count == -1:
                LL[i] = -1
            else:
                LL[i] = stack[count]
            
            stack.append(i)
            count += 1
        
        max_area = 0
        for i in range(histLen):
            width = (RL[i] - LL[i]) - 1
            area = histogram[i] * width
            
            max_area = max(max_area, area)        
        
        return max_area

if __name__ == '__main__':

    histogram = [6,2,5,4,5,1,6]
    maxArea = getMaxArea(histogram)
    print("Max Area ", maxArea)