#Time complexity for the algorithms below will be O(N)
#Space complexity will be O(1)
def pair_with_target_sum(arr, target):
    start, end = 0, len(arr) - 1
    for idx in range(len(arr)):
        sum = arr[start] + arr[end]
        if sum == target:
            return [start, end]
        
        if sum > target:
            end -= 1 # we need a pair with a bigger sum
        else:
            start += 1 # we need a pair with a smaller sum

    return [-1, -1]


def pair_with_target_sum_2(arr, target_sum):
    left, right = 0, len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


# Alternate Solution --> without using 2 pointers approach
#Time complexity for the algorithm below will be O(N)
#Space complexity will be O(N)

def target_sum_pair(arr, target_sum):
    nums = {}
    
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        
        nums[arr[i]] = i
    
    return [-1, -1]


result = pair_with_target_sum([1, 2, 3, 4, 6], 6) #Expected Output: [1, 3]
print("indexes for target sum - 6: ", result)

result_2 = pair_with_target_sum_2([2, 5, 9, 11], 11) #Expected Output: [0, 2]
print("indexes for target sum - 6: ", result_2)


#Alternate Solution Test
result_3 = target_sum_pair([1, 2, 3, 4, 6], 6) #Expected Output: [1, 3]
print("indexes for target sum - 6: ", result_3)

result_4 = target_sum_pair([2, 5, 9, 11], 11) #Expected Output: [0, 2]
print("indexes for target sum - 6: ", result_4)
