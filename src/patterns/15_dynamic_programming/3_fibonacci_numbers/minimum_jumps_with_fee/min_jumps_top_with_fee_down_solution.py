# Brute Force Solution
# Time Complexity O(3^n)
# Space Complexity O(n)
def find_min_fee(fee):
    return find_min_recursive(fee, len(fee), 0)
    
    
def find_min_recursive(fee, arr_len, step):
    if step == arr_len - 1:
        return fee[step]
    
    if step >= arr_len:
        return 0
    
    curr_fee = fee[step]
    take_step_1 = curr_fee + find_min_recursive(fee, arr_len, step+1)
    take_step_2 = curr_fee + find_min_recursive(fee, arr_len, step+2)
    take_step_3 = curr_fee + find_min_recursive(fee, arr_len, step+3)

    return min(take_step_1, take_step_2, take_step_3)


# Optimal DP Solution Using Top Down Approach
# Time Complexity O(n)
# Space Complexity O(n)
def find_min_fee_dp(fee):
    n = len(fee)
    dp = [0 for _ in range(n)]
    return find_min_recursive_dp(dp, fee, n, 0)

def find_min_recursive_dp(dp, fee, arr_len, step):
    if step == arr_len - 1:
        return fee[step]
    
    if step >= arr_len:
        return 0
    
    if dp[step] != 0:
        return dp[step]
    
    curr_fee = fee[step]
    take_step_1 = curr_fee + find_min_recursive_dp(dp, fee, arr_len, step+1)
    take_step_2 = curr_fee + find_min_recursive_dp(dp, fee, arr_len, step+2)
    take_step_3 = curr_fee + find_min_recursive_dp(dp, fee, arr_len, step+3)
    
    dp[step] = min(take_step_1, take_step_2, take_step_3)
    return dp[step]

def main():
    print("Recursive Solution Without Memoization")
    print(find_min_fee([1, 2, 5, 2, 1, 2]))
    print(find_min_fee([2, 3, 4, 5]))

    print("\n\nRecursive Solution With Memoization")
    print(find_min_fee_dp([1, 2, 5, 2, 1, 2]))
    print(find_min_fee_dp([2, 3, 4, 5]))

main()