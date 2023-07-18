# Time O(2^N)
# Space O(N)
def frog_jump(nums):

    def jump_recursive(i, n):
        if i >= n-1: return 0

        left = abs(nums[i] - nums[i+1]) + jump_recursive(i+1, n)
        right = float('inf')
        if i+2 < n:
            right = abs(nums[i] - nums[i+2]) + jump_recursive(i+2, n)

        return min(left, right)
    n = len(nums)
    return jump_recursive(0, n)


print(frog_jump([10, 50, 10])) # 0
print(frog_jump([10, 20, 30, 10]))  # 20
print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))  # 7
print(frog_jump([4, 8, 3, 10, 4, 4]))  # 2
print("\n\n")

# Time O(N)
# Space O(N) + O(N) -> recursion stack + memoization space used
def frog_jump_memo(nums):

    def jump_recursive(i, n, dp):
        if i >= n-1: return 0
        if dp[i] != -1: 
            return dp[i]

        left = abs(nums[i] - nums[i+1]) + jump_recursive(i+1, n, dp)
        
        right = float('inf')
        if i+2 < n:
             right = abs(nums[i] - nums[i+2]) + jump_recursive(i+2, n, dp)

        dp[i] = min(left, right)
        return dp[i]
    
    n = len(nums)
    dp = [-1] * (n+1)
    return jump_recursive(0, n, dp)



print(frog_jump_memo([10, 50, 10])) # 0
print(frog_jump_memo([10, 20, 30, 10]))  # 20
print(frog_jump_memo([7, 4, 4, 2, 6, 6, 3, 4]))  # 7
print(frog_jump_memo([4, 8, 3, 10, 4, 4]))  # 2
print(frog_jump_memo([5, 2, 8, 1, 3, 6])) # 9
print(frog_jump_memo([1, 2, 1, 3, 2])) # 1
print(frog_jump_memo([10, 5, 15])) # 5
print(frog_jump_memo([30, 10, 60, 10, 60, 50]))  # 40