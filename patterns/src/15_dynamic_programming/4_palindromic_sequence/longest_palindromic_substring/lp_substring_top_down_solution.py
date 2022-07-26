def find_LPS_length(str):
    n = len(str)
    return find_LPS_length_recursive(str, 0, n-1)


def find_LPS_length_recursive(str, start_idx, end_idx):
    if start_idx > end_idx:
        return 0
    
    if start_idx == end_idx:
        return 1
    
    if str[start_idx] == str[end_idx]:
        remaining_length = end_idx - start_idx - 1
        if remaining_length == find_LPS_length_recursive(str,  start_idx + 1, end_idx - 1):
            return remaining_length + 2
         
    
    l1 = find_LPS_length_recursive(str,  start_idx + 1, end_idx)
    l2 = find_LPS_length_recursive(str,  start_idx, end_idx - 1)
    
    return max(l1, l2)
    

def find_LPS_length_dp(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    
    return find_LPS_length_recursive_dp(dp, str, 0, n-1)

def find_LPS_length_recursive_dp(dp, str, start_idx, end_idx):
    if start_idx > end_idx:
        return 0

    if start_idx == end_idx:
        return 1

    if dp[start_idx][end_idx] != -1:
        return dp[start_idx][end_idx]

    if str[start_idx] == str[end_idx]:
        remaining_length = end_idx - start_idx - 1
        
        if remaining_length == find_LPS_length_recursive_dp(dp, str, start_idx + 1, end_idx - 1):
            dp[start_idx][end_idx] = remaining_length + 2
            return dp[start_idx][end_idx]

    l1 = find_LPS_length_recursive_dp(dp, str, start_idx + 1, end_idx)
    l2 = find_LPS_length_recursive_dp(dp, str, start_idx, end_idx - 1)
    dp[start_idx][end_idx] = max(l1, l2)

    return dp[start_idx][end_idx]


def main():
    print("Recursive Solution Without Memoization")
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))
    
    print("\n\nRecursive Solution With Memoization")
    print(find_LPS_length_dp("abdbca"))
    print(find_LPS_length_dp("cddpd"))
    print(find_LPS_length_dp("pqr"))
    
main()