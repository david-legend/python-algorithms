from math import sqrt
from bintrees import RBTree

class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * sqrt(2)
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val

# Time O(klogk) | Space O(k)
def generate_first_k_a_b_sqrt2(k):
    # Initial for 0 + 0 * sqrt(2).
    candidates = RBTree([(ABSqrt2(0,0), None)])
    result = []

    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)

        candidates[ABSqrt2(next_smallest.a + 1, next_smallest.b)] = None
        candidates[ABSqrt2(next_smallest.a, next_smallest.b + 1)] = None
    
    return result



print(generate_first_k_a_b_sqrt2(4))
print(generate_first_k_a_b_sqrt2(5))
print(generate_first_k_a_b_sqrt2(6))
print(generate_first_k_a_b_sqrt2(8))
