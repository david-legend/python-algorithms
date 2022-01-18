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



print(backspace_compare(str1="xy#z", str2="xzz#"))
print(backspace_compare(str1="xy#z", str2="xyz#"))
print(backspace_compare(str1="xp#", str2="xyz##"))
print(backspace_compare(str1="xywrrmp", str2="xywrrmu#p"))