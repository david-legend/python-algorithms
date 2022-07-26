# Brute Force Solution
# Time Complexity O(2^n)
# Space Complexity O(n)
def find_max_steal(wealth):
    n = len(wealth)
    return find_max_steal_recursive(wealth, n, 0)

def find_max_steal_recursive(wealth, arr_len, curr_house):
    if curr_house >= arr_len:
        return 0
    
    steal_current = wealth[curr_house] + find_max_steal_recursive(wealth, arr_len, curr_house+2)
    skip_current = find_max_steal_recursive(wealth, arr_len, curr_house+1)
    
    return max(steal_current, skip_current)


# Optimal DP Solution Using Top Down Approach
# Time Complexity O(n)
# Space Complexity O(n)
def find_max_steal_dp(wealth):
    n = len(wealth)
    dp = [0 for _ in range(n)]
    return find_max_steal_recursive_dp(dp, wealth, n, 0)
    
def find_max_steal_recursive_dp(dp, wealth, arr_len, curr_house):
    if curr_house >= arr_len:
        return 0
    
    if dp[curr_house] != 0:
        return dp[curr_house]
    
    steal_current = wealth[curr_house] + find_max_steal_recursive_dp(dp, wealth, arr_len, curr_house+2)
    skip_current = find_max_steal_recursive_dp(dp, wealth, arr_len, curr_house+1)
    dp[curr_house] = max(steal_current, skip_current)
    return dp[curr_house]


def main():

    print("Recursive Solution Without Memoization")
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))

    print("\n\nRecursive Solution With Memoization")
    print(find_max_steal_dp([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_dp([2, 10, 14, 8, 1]))

main()