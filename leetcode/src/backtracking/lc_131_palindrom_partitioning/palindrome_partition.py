def partition(s):
    result = []
    partition_helper(s, result, [], 0)
    return result


def partition_helper(s, result, path, idx):
    if idx == len(s):
        result.append(list(path))
        return
    
    for i in range(idx, len(s)):
        if(isPalindrome(idx, i, s)):
            path.append(s[idx : i+1])
            partition_helper(s, result, path, i+1)
            path.pop()

def isPalindrome(start, end, s):
    while start <= end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            return False
        
    return True
print(partition("aa")) # [["a"]]
print(partition("aab")) # [["a","a","b"],["aa","b"]]
print(partition("abba")) # [['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']]
print(partition("aabb")) # [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]