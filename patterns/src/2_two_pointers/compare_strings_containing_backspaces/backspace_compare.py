def backspace_compare(str1, str2):
    return get_str(str1) == get_str(str2)

def get_str(str1):
    result = ""
    for char in str1:
        if char != "#":
            result += char
        else:
            result = result[: len(result)-1]

    return result



print(backspace_compare(str1="xy#z", str2="xzz#"))  #True
print(backspace_compare(str1="xy#z", str2="xyz#"))  #False
print(backspace_compare(str1="xp#", str2="xyz##"))  #True
print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))  #True
print("\n\n")

# Solution 2
def compare(s1, s2):
    def parse_str(s):
        result = []
        for char in s:
            if char != "#":
                result.append(char)
            else:
                if result: result.pop()
        return result
    
    return parse_str(s1) == parse_str(s2)

print(compare(s1="xy#z", s2="xzz#"))    # True
print(compare(s1="xy#z", s2="xyz#"))    # False
print(compare(s1="xp#", s2="xyz##"))    # True
print(compare(s1="xywrrmp", s2="xywrrmu#p"))    # True