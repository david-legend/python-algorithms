def find_substring(str, pattern):
    match, window_start = 0,0
    char_freq = {}
    found = ""
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
        
    char_freq_length = len(char_freq)
    
    for window_end in range(len(str)):
        right_char = str[window_end]
           
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if (char_freq[right_char] >= 0):
                found += right_char
            
            if char_freq[right_char] == 0:
                match += 1
                
            if char_freq[right_char] < 0:
                window_start = max(window_start, window_end)
                for char in found:
                    char_freq[char] += 1
                found = ""
                match = 1
        
        if match == char_freq_length:
            return str[window_start: window_end+1]   

    return ""


print(find_substring("aabdec", "abc"))
print(find_substring("abdbca", "abc"))
print(find_substring("adcad", "abc"))