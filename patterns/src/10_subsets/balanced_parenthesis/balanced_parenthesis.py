from collections import deque


class ParenthesesString:
    def __init__(self, str, open_count, close_count):
        self.str = str
        self.open_count = open_count
        self.close_count = close_count
    
def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    
    while queue:
        ps = queue.popleft()
        
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.str)
        else:
            if ps.open_count < num:
                queue.append(
                    ParenthesesString(ps.str + "(", ps.open_count + 1, ps.close_count))
            
            if ps.close_count < ps.open_count:
                queue.append(
                    ParenthesesString(ps.str + ")", ps.open_count, ps.close_count + 1))
        
    return result




print("All combinations of balanced parentheses are: " +
    str(generate_valid_parentheses(2)))
print("All combinations of balanced parentheses are: " +
    str(generate_valid_parentheses(3)))

