def longestPalindromicSubstring(s: str):

    string_length =  len(s)
    res = ''
    res_len = 0

    for i in range(string_length):
        # odd length
        l , r = i, i
        while l > -1 and r < string_length and s[l] == s[r]:
            curr_len =  r - l + 1

            if curr_len > res_len:
                res_len = curr_len
                res = s[l: r+1]

            l -= 1
            r += 1

        # even length
        l, r = i, i+1
        while l > -1 and r < string_length and s[l] == s[r]:
            curr_len =  r - l + 1

            if curr_len > res_len:
                res_len = curr_len
                res = s[l: r+1]

            l -= 1
            r += 1
        
    return res
       
if __name__ == '__main__':
    
    string = 'babad'
    longest_sub_string_len = longestPalindromicSubstring(string)
    print("Longest Substring is ", longest_sub_string_len)

