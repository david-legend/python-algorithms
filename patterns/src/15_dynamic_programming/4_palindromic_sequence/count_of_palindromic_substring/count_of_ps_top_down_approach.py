def count_PS(s):
    n, dp = len(s), {}
    count = 0

    def count_PS_recursive(start_idx, end_idx):
        nonlocal count
        if start_idx > end_idx:
            return
        
        if start_idx == end_idx:
            if str(start_idx) not in dp:
                count += 1
                dp[str(start_idx)] = True
            return
        
        if s[start_idx] == s[end_idx]:
            key = str(start_idx) + ',' + str(end_idx)
            if end_idx - start_idx <= 2 and key not in dp:
                count += 1
                dp[key] = True
            count_PS_recursive(start_idx + 1, end_idx - 1)
        
        count_PS_recursive(start_idx + 1, end_idx)
        count_PS_recursive(start_idx, end_idx - 1)

    count_PS_recursive(0, n-1)
    # print(dp)
    return len(dp)





# def main():
#     print("Recursive Solution Without Memoization")
#     # print(count_PS("aaaaa")) # result --> 6
#     print(count_PS("aaa")) # result --> 6
#     print(count_PS("abdbca")) # result --> 7
#     print(count_PS("cddpd")) # result --> 7
#     print(count_PS("pqr")) # result --> 3

    
# main()



#Iterative
def countSubstrings(s: str) -> int:
    count = 0

    for i in range(len(s)):
        count += isPalindrome(i, i, s)
        count += isPalindrome(i, i+1, s)
    
    return count
    
def isPalindrome(l, r, s):
    count = 0
    while l >= 0 and r < len(s) and l <= r:
        if s[l] != s[r]: break
        count += 1
        l -= 1
        r += 1
    return count

print(countSubstrings("abc"))
print(countSubstrings("abdbca"))
print(countSubstrings("cddpd"))
print(countSubstrings("pqr"))