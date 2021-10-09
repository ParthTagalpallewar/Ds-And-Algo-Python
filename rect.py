# Count pairs of similar rectangles possible from a given array

# Given a 2D array A[][2] of size N (1 ≤ N ≤ 103), where A[i][0] and A[i][1] 
# denotes the length and breadth of rectangle i respectively.

#Two rectangle i and j where (i < j) are similar if the ratio of 
# their length and breadth is equal


# Input : A[][2] = {{4, 8}, {15, 30}, {3, 6}, {10, 20}}
# Output: 6
# Explanation: Pairs of similar rectangles are (0, 1), {0, 2), (0, 3), (1, 2), (1, 3), (2, 3). For every rectangle, ratio of length : breadth is 1 : 2

# Input : A[][2] = {{2, 3}, {4, 5}, {7, 8}}
# Output: 0
# Explanation: No pair of similar rectangles exists.


def getCount(sides):# {{4, 8}, {15, 30}, {3, 6}, {10, 20}}
     
    pairs = 0
 
    for i in range(len(sides)): # [1, 2]
        for j in range(i + 1, len(sides)): # [3, 4]
            # if (1 / 3) == (2 / 4)
            if (sides[i][0] / sides[j][0] == sides[i][1] / sides[j][1]):
                pairs += 1
                 
    return pairs