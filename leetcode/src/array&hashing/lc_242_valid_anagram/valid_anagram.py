def isAnagram(s, t) -> bool:
    if len(s) != len(t): return False
    char_freq = {}

    for i in range(len(s)):
        st_1, st_2 = s[i], t[i]
        char_freq[st_1] = char_freq.get(st_1, 0) + 1
        char_freq[st_2] = char_freq.get(st_2, 0) - 1
        
        if st_2 in char_freq and char_freq.get(st_1, 0) == 0: 
            del char_freq[st_1]
        if st_2 in char_freq and char_freq[st_2] == 0: 
            del char_freq[st_2]
    
    return True if len(char_freq) == 0 else False


def isAnagram2(s, t) -> bool:
    if len(s) != len(t): return False

    char_count = {}
    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
        char_count[t[i]] = char_count.get(t[i], 0) - 1

    for count in char_count.values():
        if count != 0: return False

    return True