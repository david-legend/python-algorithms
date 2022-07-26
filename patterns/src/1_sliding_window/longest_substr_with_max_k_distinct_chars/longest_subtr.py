# Time complexity of the algorithm is O(N+N), 
# which is asymptotically equivalent to O(N)

# space complexity is O(K)

def longest_substring_with_k_distinct(str, k):
    max_len = 0
    start = 0
    distinct_chars = {}
    
    for window_end in range(len(str)):
        curr_char = str[window_end]
        if curr_char not in distinct_chars:
            distinct_chars[curr_char] = 0
        
        distinct_chars[curr_char] += 1
        
        while len(distinct_chars) > k:
            left_char = str[start]
            distinct_chars[left_char] -= 1
            if distinct_chars[left_char] == 0:
                del distinct_chars[left_char]
            
            start += 1
            
        max_len = max(max_len, window_end - start + 1)
        
    return max_len


result1 = longest_substring_with_k_distinct("cbbebi", 10)   
print("Longest substring with at least maximum of 10 distinct chars: ", result1)       

result2 = longest_substring_with_k_distinct("araaci", 3)   
print("Longest substring with at least maximum of 3 distinct chars: ", result2)          

result3 = longest_substring_with_k_distinct("araaci", 2)   
print("Longest substring with at least maximum of 2 distinct chars: ", result3)       

result4 = longest_substring_with_k_distinct("araaci", 1)   
print("Longest substring with at least maximum of 1 distinct chars: ", result4)   

result5 = longest_substring_with_k_distinct("cbbebi", 3)   
print("Longest substring with at least maximum of 3 distinct chars: ", result5)       