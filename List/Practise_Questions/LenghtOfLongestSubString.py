def lengthOfLongestSubstring(s: str) -> int:
        
        longestSubString = 0
        current_len = 0
        
        char_tracker = dict()

        itr = 0
        while itr < len(s):
            i = s[itr]
            # if char seen for first time then add to dict
            if char_tracker.get(i) is None:
                char_tracker[i] = itr

                # moving forward and counting sum
                current_len += 1
                itr += 1
            
            # if char is get repeated
            else:
                # start iteration from previous repeated char
                itr = char_tracker.get(i) + 1
                longestSubString = max(longestSubString, current_len)
                current_len = 0
                char_tracker.clear()

        longestSubString = max(longestSubString, current_len)
        
        return longestSubString

if __name__ == '__main__':
    
    string = "abcabcbb"
    length = lengthOfLongestSubstring(string)
    print("Length is ", length)