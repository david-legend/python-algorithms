# IsPalindrome --> Write a recursive function if the string passed to is a palindrome, otherwise return false

def isPalindrome(str):
    strLength = len(str)
    assert strLength > 0, "Length of string should be greater than 0"

    # if initial length of string is one -> it definitely a palindrome
    # Also handles, the last letter in an odd length palindrome
    if strLength == 1:
        return True

    if str[0] == str[strLength - 1]:
        # handles even length palindromes
        if(len(str) == 2):
            return True
        else:
            return isPalindrome(str[1: (strLength - 1)])
    else:
        return False


# TEST

# OddLength Palindromes
print(isPalindrome("racecar"))                      #ans --> True
print(isPalindrome("awesome"))                      #ans --> False
print(isPalindrome("level"))                        #ans --> True
print(isPalindrome("madam"))                        #ans --> True
print(isPalindrome("kayak"))                        #ans --> True
print(isPalindrome("tacocat"))                      #ans --> True
print(isPalindrome("foobar"))                       #ans --> False
print(isPalindrome("amanaplanacanalpanama"))        #ans --> True
print(isPalindrome("amanaplanacanalpandemonium"))   #ans --> False

# Even Length Palindromes
print(isPalindrome("12344321"))   #ans --> True
print(isPalindrome("12345321"))   #ans --> False