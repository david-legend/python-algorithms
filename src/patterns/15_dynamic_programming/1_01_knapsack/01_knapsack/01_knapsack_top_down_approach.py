# Recursive Brute Force Approach
def solve_knapsack(profits, weights, capacity):
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, curr_index):
    if capacity <= 0 or curr_index >= len(profits):
        return 0
     
    profit_1 = 0
    if weights[curr_index] <= capacity:
        profit_1 = profits[curr_index] + knapsack_recursive(profits, weights, capacity - weights[curr_index], curr_index+1)
    
    profit_2 = knapsack_recursive(profits, weights, capacity, curr_index + 1)
    
    return max(profit_1, profit_2)


# Optimal DP Approach
def solve_knapsack_dp(profits, weights, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return knapsack_recursive_dp(dp, profits, weights, capacity, 0)

def knapsack_recursive_dp(dp, profits, weights, capacity, curr_index):
    # base checks
    if capacity <= 0 or curr_index >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[curr_index][capacity] != -1:
        return dp[curr_index][capacity]

    # recursive call after choosing the element at the curr_index
    # if the weight of the element at curr_index exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[curr_index] <= capacity:
        profit1 = profits[curr_index] + knapsack_recursive_dp(
        dp, profits, weights, capacity - weights[curr_index], curr_index + 1)

    # recursive call after excluding the element at the curr_index
    profit2 = knapsack_recursive_dp(
        dp, profits, weights, capacity, curr_index + 1)

    dp[curr_index][capacity] = max(profit1, profit2)
    return dp[curr_index][capacity]

def main():
    # Brute Force
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    # print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    
    # Optimal Approach
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_dp([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()