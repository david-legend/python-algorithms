from itertools import permutations


from collections import deque

# Time complexity O(N*N!)
# We know that there are a total of N! permutations of a set with ‘N’ numbers. 
# In the algorithm below, we are iterating through all of these permutations 
# with the help of the two ‘for’ loops. In each iteration, we go through all 
# the current permutations to insert a new number in them on line 27. 
# To insert a number into a permutation of size ‘N’ will take O(N), 
# which makes the overall time complexity of our algorithm O(N*N!).

# Space complexity O(N*N!)
# All the additional space used by our algorithm is for the result list and the queue 
# to store the intermediate permutations. If you see closely, at any time, 
# we don’t have more than N! permutations between the result list and the queue. 
# Therefore the overall space complexity to store N! 
# permutations each containing N elements will be O(N*N!).

def find_permutations(nums):
    nums_length = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for curr_num in nums:
        n = len(permutations)
        
        for _ in range(n):
            prev_permutation = permutations.popleft()
            
            for j in range(len(prev_permutation) + 1):
                new_permutation = list(prev_permutation)
                new_permutation.insert(j, curr_num)
                
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    return result       


print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
print("Here are all the permutations: " + str(find_permutations([1, 2, 3, 4])))