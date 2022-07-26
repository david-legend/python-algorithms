# Time complexity of the algorithm is O(N+N), 
# which is asymptotically equivalent to O(N)

# space complexity is O(K), where K is the number of baskets
def fruits_into_baskets(fruits):
    baskets = 2
    max_length = 0
    start = 0
    distinct_fruits = {}
    
    for window_end in range(len(fruits)):
        curr_fruit_tree = fruits[window_end]
        if curr_fruit_tree not in distinct_fruits:
            distinct_fruits[curr_fruit_tree] = 0
            
        distinct_fruits[curr_fruit_tree] += 1
        
        while len(distinct_fruits) > baskets:
            left = fruits[start]
            distinct_fruits[left] -= 1
            
            if distinct_fruits[left] == 0:
                del distinct_fruits[left]
            
            start += 1
        
        max_length = max(max_length, window_end - start + 1)

    if max_length == 0:
        return -1
    
    return max_length


print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))) #Output 3
print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))) #Output 5

