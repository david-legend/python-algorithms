def wordBreak(s, wordDict):
    str_len = len(s)
    dp = [False] * (len(s) + 1)
    dp[str_len] = True

    for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
            if i + len(word) <= str_len and s[i : i + len(word)] == word:
                dp[i] = dp[i+len(word)]
            if dp[i]:
                break
    return dp[0]


def wordBreak2(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    wordDict = set(wordDict)

    for i in range(1, n + 1):
        for j in range(i):
            curr_word = s[j:i] 
            if dp[j] and curr_word in wordDict:
                dp[i] = True
                break
            
    return dp[n]

print(wordBreak2("leetcode", ["leet", "code"]))