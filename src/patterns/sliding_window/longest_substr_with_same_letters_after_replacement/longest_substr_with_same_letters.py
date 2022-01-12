#Time complexity will be O(N).

#Space complexity O(1) 
#As we expect only the lower case letters in the input string, 
#we can conclude that the space complexity will be O(26) 
#to store each letter’s frequency in the HashMap, 
#which is asymptotically equal to O(1).

def length_of_longest_substring(str, k):
    max_length, window_start = 0, 0
    max_repeat_letter_count = 0
    char_frequency_map = {}
    
    for window_end in range(len(str)):
        curr_char = str[window_end]
        
        if curr_char not in char_frequency_map:
            char_frequency_map[curr_char] = 0
            
        char_frequency_map[curr_char] += 1
        
        max_repeat_letter_count = max(max_repeat_letter_count
                                      , char_frequency_map[curr_char])
        
        if window_end - window_start + 1 - max_repeat_letter_count > k:
            left_char = str[window_start]
            char_frequency_map[left_char] -= 1
            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)
            
    return max_length



print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))
        
    