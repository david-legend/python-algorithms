def find_string_anagrams(str, pattern):
    result_indexes = []
    window_start, match  = 0, 0
    pattern_length = len(pattern)
    char_freq = {}
    
    
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1
       
    char_freq_len = len(char_freq)
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                match += 1
        
        if match == char_freq_len:
            result_indexes.append(window_start)
            
        if window_end >= pattern_length - 1:
            left_char = str[window_start]
            window_start += 1
            
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    match -= 1
                char_freq[left_char] += 1
    
    return result_indexes
    
    
print(find_string_anagrams("ppqp","pq"))
print(find_string_anagrams("abbcabc","abc"))