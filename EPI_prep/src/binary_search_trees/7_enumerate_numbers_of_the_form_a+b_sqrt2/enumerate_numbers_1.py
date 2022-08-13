from math import sqrt

class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * sqrt(2)
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __eq__(self, other):
        return self.val == other.val


# Time O(n)
def generate_first_k_a_b_sqrt2(k):
    # Will store the first k nunbers of the forn a + b sqrt(2)
    candidates = [ABSqrt2(0,0)]
    i = j = 0
    for _ in range(1, k):
        candiate_i = ABSqrt2(candidates[i].a + 1, candidates[i].b)
        candiate_j = ABSqrt2(candidates[j].a, candidates[j].b + 1)
        candidates.append(min(candiate_i, candiate_j))
        if candidates[-1].val == candiate_i.val:
            i += 1
        
        if candidates[-1].val == candiate_j.val:
            j += 1
        
    return [data.val for data in candidates]



print(generate_first_k_a_b_sqrt2(4))
print(generate_first_k_a_b_sqrt2(5))
print(generate_first_k_a_b_sqrt2(6))
print(generate_first_k_a_b_sqrt2(8))
