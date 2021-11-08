arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]
n = len(arr)
D = 5

s = 0
b = 0
value = 0

arr = sorted(arr)
print(arr)

# for i in range(n):
#     for j in range(n):
#         if i != j:
#             small = arr[i] + D
#             bigger = arr[j] - D

#             current = bigger - small
#             print(current)
#             if value < current:
#                 s = small
#                 b = bigger
#                 value = value

# print("smaller ", s + D)
# print("Bigger ", b - D)
# print("value ", value)
