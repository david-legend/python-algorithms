# Time Complexity O(n)
# Space Complexity O(n)
def balancedBrackets (string):
    openingBrackets = "({["
    closingBrackets = ")}]"
    matchingBrackets = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            elif stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print("([])(){}(())()(): ", balancedBrackets("([])(){}(())()()"))
print("{}gawgw(): ", balancedBrackets("{}gawgw()"))
print("(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(()): ", balancedBrackets("(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())"))
print("()[]{}{: ", balancedBrackets("()[]{}{"))
print("[((([])([]){}){}){}([])[]((()): ", balancedBrackets("[((([])([]){}){}){}([])[]((())"))
print("(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}})))))): ", balancedBrackets("(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}}))))))"))
