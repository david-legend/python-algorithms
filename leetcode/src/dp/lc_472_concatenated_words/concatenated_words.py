def findAllConcatenatedWordsInADict(words):
    result, wordDict = [], set(words)
    for word in words:
        if wordBreak(word, wordDict):
            result.append(word)

    return result
    
def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            curr_word = s[j:i] 
            if dp[j] and curr_word in wordDict and curr_word != s:
                dp[i] = True
                break
            
    return dp[n]