def find_permutation(str, pattern):
    pattern_length = len(pattern)
    matched, window_start = 0,0
    char_freq = {}
    
    for char in pattern:
        if char not in char_freq:
            char_freq[char]  = 0
        char_freq[char] += 1
    
    char_freq_length =  len(char_freq)
        
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1
        
        if matched == char_freq_length:
            return True
        
        if window_end >= pattern_length - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    
    return False
    
    


print(find_permutation("aaacb", "abc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))
print(find_permutation("odicf", "dc"))
print(find_permutation("oidbcaf", "abc"))