# Time complexity O(N*2^N)
# Since, in each step, the number of subsets doubles 
# as we add each element to all the existing subsets, 
# therefore, we will have a total of O(2^N) subsets, 
# where ‘N’ is the total number of elements in the input set. 
# And since we construct a new subset from an existing set, 
# therefore, the time complexity of the above algorithm will be O(N*2^N)

# Space complexity O(N*2^N)
# All the additional space used by our algorithm is for the output list. 
# Since we will have a total of O(2^N) subsets, and each subset can take up to 
# O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).

def find_subsets(nums):
    subsets = []
    subsets.append([])
    
    for curr_number in nums:
        n = len(subsets)
        
        for i in range(n):
            set_1 = list(subsets[i])
            set_1.append(curr_number)
            subsets.append(set_1)
            
    return subsets
            

print("Here is the list of subsets: " + str(find_subsets([1, 3])))
print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))