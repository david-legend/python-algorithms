def test_dsa(s, t):
    def getDistinctCount(i, chars):
        if i == len(s):
            result = "".join(chars)
            if result == t:
                return 1
            return 0
        
        chars.append(s[i])
        left = getDistinctCount(i+1, chars)

        chars.pop()
        right = getDistinctCount(i+1, chars)

        return left + right
        
    return getDistinctCount(0, [])

print(test_dsa(s = "rabbbit", t = "rabbit"))
print(test_dsa( s = "babgbag", t = "bag"))

    