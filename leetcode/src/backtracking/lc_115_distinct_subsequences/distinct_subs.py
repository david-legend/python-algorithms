def numDistinct(s, t):
    def count(i, chars):
        if len(s) == i:
            result = "".join(chars)
            if result == t:
                return 1
            return 0

        chars.append(s[i])
        i += 1
        left = count(i, chars)

        chars.pop()
        right = count(i, chars)

        return left + right
    
    return count(0, [])

print(numDistinct(s = "rabbbit", t = "rabbit")) #3
print(numDistinct(s = "babgbag", t = "bag")) #5