# Time complexity of the algorithm is O(N+N), 
# which is asymptotically equivalent to O(N)

# space complexity is O(N=K), 
# where K is the number of distinct characters in the input string. 
# This also means K <= N, because in the worst case, 
# the whole string might not have any duplicate character

def non_repeat_substring(str):
    start = 0
    max_length = 0
    distinct_chars = {}
    
    for window_end in range(len(str)):
        curr_str = str[window_end]
        
        if curr_str not in distinct_chars:
            distinct_chars[curr_str] = 0
        
        distinct_chars[curr_str] += 1
        
        while distinct_chars[curr_str] > 1:
            left_char = str[start]
            distinct_chars[left_char] -= 1
            
            if distinct_chars[left_char] == 0:
                del distinct_chars[left_char]
            
            start += 1
            
        max_length = max(max_length, window_end - start + 1)
        
    
    return max_length

#Solution 2 -> beautiful
# which is asymptotically equivalent to O(N)

# space complexity is O(N=K), 
# where K is the number of distinct characters in the input string. 
# This also means K <= N, because in the worst case, 
# the whole string might not have any duplicate character

def non_repeat_substring_2(str):
    window_start = 0
    max_length = 0
    char_index_map = {}
    
    for window_end in range(len(str)):
        curr_char = str[window_end]
        # if the map already contains the 'curr_char', shrink the window from the beginning so that
        # we have only one occurrence of 'curr_char'
        if curr_char  in char_index_map:
            # this is tricky; in the current window, we will not have any 'curr_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'curr_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[curr_char] + 1)

        # insert the index 'curr_char' into the map
        char_index_map[curr_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
        
    
    return max_length

print("Output: ", non_repeat_substring("aabccbb")) #Output: 3
print("Output: ", non_repeat_substring("abbbb")) #Output: 2
print("Output: ", non_repeat_substring("abccde")) #Output: 3

print("Length of the longest substring: " + str(non_repeat_substring_2("aabccbb")))
print("Length of the longest substring: " + str(non_repeat_substring_2("abbbb")))
print("Length of the longest substring: " + str(non_repeat_substring_2("abccde")))