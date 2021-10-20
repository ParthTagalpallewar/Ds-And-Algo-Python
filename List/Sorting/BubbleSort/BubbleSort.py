def bubblesort(list):
    
# Swap the elements to arrange in order
   for iter_num in range(len(list)-1, 0, -1):
      for idx in range(iter_num):
         print("j ", idx , "   num ", list[idx], "   idx+i ", list[idx+1])
         if list[idx]>list[idx+1]:
            list[idx] ,list[idx+1] = list[idx+1], list[idx]

list = [3, 6, 2, 1, 9, 8, 7]
bubblesort(list)
print(list)
