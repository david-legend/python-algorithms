# Reverse --> Write a recursive function that accepts a string and returns a new string in reverse

def reverse(str):
    strLength = len(str)
    assert strLength > 0, "String must have a length greater than zero"
    if(strLength == 1):
        return str[0]
    else:
        return str[strLength - 1] + reverse(str[ : (strLength - 1)])


print(reverse("python"))        #ans --> nohtyp
print(reverse("appmillers"))    #ans --> srellimppa