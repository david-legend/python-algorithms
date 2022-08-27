def can_partion_k_subsets(nums, k):
    total_sum, size = sum(nums), len(nums)
    if total_sum % k > 0:
        return False

    target = total_sum / k
    used_values = [False] * size
    def backtrack(i, k, subset_sum):
        if k == 0:
            return True
        
        if subset_sum == target:
            return backtrack(0, k-1, 0)
        
        for j in range(i, size):
            curr_val = nums[j]
            if used_values[j] or curr_val + subset_sum > target:
                continue
            used_values[j] = True

            if backtrack(j+1, k, curr_val + subset_sum):
                return True
            
            used_values[j] = False
        
        return False

    return backtrack(0, k, 0)





print(can_partion_k_subsets([4,3,2,3,5,2,1], 4)) # True
print(can_partion_k_subsets([4,3,2,3,5,2,1], 5)) # False
print(can_partion_k_subsets([1,2,3,4], 3)) # False

#  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         used = [False]*len(nums)
#         total_sum = sum(nums)
#         if total_sum % k != 0:
#             return False
#         target = total_sum // k
#         nums.sort(reverse = True)
        
#         #sorting the array in descending order
#         #so if first value is greater than target, it will not be included in any subset
#         #so we cant partition the entire array into k equal sum subsets
#         if nums[0] > target:
#             return False
        
#         dp = {}
#         def backtrack(i,k,rem):
#             #since subproblem depends on used indices of array
#             #if same subproblem occurs again just return dp value
#             if tuple(used) in dp:
#                 return dp[tuple(used)]
#             if k == 0:
#                 return True
#             if rem == 0:
#                 partition = backtrack(0,k-1,target)
#                 dp[tuple(used)] = partition
#                 return partition
#             for j in range(i,len(nums)):
#                 if not used[j] and rem-nums[j] >= 0:
#                     used[j] = True
#                     if backtrack(j+1,k,rem-nums[j]):
#                         return True
#                     used[j] = False
#             dp[tuple(used)] = False
#             return False
#         return backtrack(0,k,target)