# Time O(n) + O(n)
# Space O(1)
def house_robber(nums):
    n = len(nums)
    if not nums: return 0
    if n == 1: return nums[0]
    with_first, without_first = [], []
    for i in range(n):
        if i != 0: without_first.append(nums[i])
        if i != n-1: with_first.append(nums[i])

    return max(solve(with_first), solve(without_first))

def solve(nums):
    n = len(nums)
    curr, prev, prev2 = 0, nums[0], 0

    for i in range(1, n):
        rob = nums[i] + (prev2 if i >  1 else 0)
        dont_rob = prev
        curr = max(rob, dont_rob)
        prev2, prev = prev, curr
    
    return prev

print(house_robber([2,3,2])) # 3
print(house_robber([1,2,3,1])) # 4
print(house_robber([1,2,3])) # 3
print("\n")


# Time O(n) + O(n)
# Space O(1)
def house_robber_optimal(nums):
    n = len(nums)
    if not nums: return 0
    if n == 1: return nums[0]
    
    return max(solve_optimal(nums, 0, len(nums) - 2), solve_optimal(nums, 1, len(nums) - 1))

def solve_optimal(nums, start, end):
    curr, prev, prev2 = 0, nums[start], 0

    for i in range(start + 1, end + 1):
        rob = nums[i] + (prev2 if i >  1 else 0)
        dont_rob = prev
        curr = max(rob, dont_rob)
        prev2, prev = prev, curr
    
    return prev


print(house_robber_optimal([2,3,2])) # 3
print(house_robber_optimal([1,2,3,1])) # 4
print(house_robber_optimal([1,2,3])) # 3