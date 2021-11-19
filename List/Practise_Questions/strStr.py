def strStr(haystack: str, needle: str):
    
    needle_len = len(needle)
    haystack_len = len(haystack)
    itr = 0
    i = 0

    if needle_len == 0:
        return 0

    while i < haystack_len:

        if haystack[i] == needle[itr]:
            itr += 1
        
        else:
            i -= itr
            itr = 0
        
        if itr == needle_len:
            return i - itr + 1
        
        i += 1
    
    return -1
    
        

if __name__ == '__main__':
    
    str = "mississippi"
    niddle = "issip"

    i = strStr(str, niddle)
    print(i)