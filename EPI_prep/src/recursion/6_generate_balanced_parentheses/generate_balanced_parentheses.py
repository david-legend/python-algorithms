from collections import deque
class Paren:
    def __init__(self, open = 0, close = 0, parens = "") -> None:
        self.open, self.close, self.paren = open, close, parens

def generate_balanced_parentheses(n):
    result = []
    if n <= 0:
        return result

    def gen_recursive(curr):
        if curr.open == n and curr.close == n:
            result.append(curr.paren)
        
        if curr.open < n:
            gen_recursive(Paren(curr.open + 1, curr.close, curr.paren + "("))

        if curr.open > curr.close and curr.close < n:
            gen_recursive(Paren(curr.open, curr.close + 1, curr.paren + ")"))
            
    gen_recursive(Paren())
    return result


print("\nRecursive Solution\n")
print(generate_balanced_parentheses(1))
print(generate_balanced_parentheses(2))
print(generate_balanced_parentheses(3))


def generate_balanced_parentheses_bfs(n):
    result = []
    if n > 0:
        queue = deque([Paren()])
        
        while queue:
            curr = queue.popleft()

            if curr.open == n and curr.close == n:
                result.append(curr.paren)
            
            if curr.open < n:
                queue.append(Paren(curr.open + 1, curr.close, curr.paren + "("))
            
            if curr.open > curr.close and curr.close < n:
                queue.append(Paren(curr.open, curr.close + 1, curr.paren + ")"))
        
    return result

print("\nBreadth First Search Solution\n")
print(generate_balanced_parentheses_bfs(1))
print(generate_balanced_parentheses_bfs(2))
print(generate_balanced_parentheses_bfs(3))


        
