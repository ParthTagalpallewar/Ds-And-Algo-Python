import string
alpha = string.ascii_lowercase

# 5-17
# 3-9
# 10-37
def srange(N):
    Clist = list(range(N))+list(range(N-2,-1,-1))
    # print(" n = {} list = {}".format(n, Clist))
    return Clist

print(list([alpha[5-j-1] for j in srange(1)]))
print("-".join(["e"]).center((4*5)-3,"-"))