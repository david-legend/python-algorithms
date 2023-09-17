# Time - O(n * 4) * 3
# Space - O(n) + O(n * 4)
def ninja_training(training):
   day_length = len(training)
   dp = [[-1, -1, -1, -1]] * day_length
   return solve(training, day_length-1, 3, dp)


def solve(training, day, prev_task, dp):
    if day == 0:
        max_result = float('-inf')
        for i in range(3):
            if i != prev_task:
                max_result = max(max_result, training[day][i])
        # dp[day][prev_task] = max_result
        return max_result
   
    if dp[day][prev_task] != -1: return dp[day][prev_task]
    max_merit = float('-inf')
    for i in range(3):
        if i != prev_task:
            max_merit =  max(max_merit, training[day][i] + solve(training, day-1, i, dp))
    dp[day][prev_task] = max_merit

    return dp[day][prev_task];


# print(ninja_training([
#     [1, 50,   4],
#     [3, 100, 11]
# ])) #104

print(ninja_training([
    [1, 2, 5],
    [3, 1, 1],
    [3, 3, 3],
])) #11

print(ninja_training([
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90],
])) #210