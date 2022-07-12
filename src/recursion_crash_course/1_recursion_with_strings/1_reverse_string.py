# (base case) At what point do i stop this function ?
# It can be stopped at the last char of the string or when there is no string to reverse
# We can also think about this as what is the smallest input that can be pass into this function -> an empty string

# (Work) what is the least amount of work we can do ?
# From the solution below we can see that we use the call stack 
# and the way we append a character to our advantage

# Below is how the call stack will look like when we execute the function,
# The magic is in the call stack and how we concatenate the return values 

# | ""       -->  "" 
# | "o"      -->  "" + "o" =  "o"
# | "lo"     -->  "o" + "l" = "ol"
# | "llo"    -->  "ol" + "l" = "oll"
# | "ello"   -->  "oll" + "e" = "olle"
# | "hello"  -->  "olle" + "h" = "olleh"

def revserse_string(s):
    if len(s) == 0:
        return ""
    
    return revserse_string(s[1:]) + s[0]

print(revserse_string("hello")) #olleh
print(revserse_string("string")) #gnirts
print(revserse_string("multiplatform")) #mroftalpitlum