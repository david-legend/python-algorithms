
# Time -> O(α(n))
# This makes disjoint-set operations practically amortized constant time
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure#:~:text=never%20accessed%20again.-,Time%20complexity,require%20O(n)%20time.

class DisjointSet:
    def __init__(self, n) -> None:
        self.parent, self.rank, self.size = [], [], []
        for i in range(n+1):
            self.rank.append(0)
            self.size.append(1)
            self.parent.append(i)
    
    def find_parent(self, node):
        if self.parent[node] == node: return node

        parent = self.find_parent(self.parent[node])
        self.parent[node] = parent
        return parent
    
    # up_u means ultimate parent of u
    # up_v means ultimate parent of v
    def union_by_rank(self, u, v):
        up_u = self.find_parent(u)
        up_v = self.find_parent(v)
        if up_u == up_v: return
        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_u] > self.rank[up_v]:
            self.parent[up_v] = up_u
        else:
            self.parent[up_v] = up_u
            self.rank[up_u] += 1
    
    def union_by_size(self, u, v):
        up_u = self.find_parent(u)
        up_v = self.find_parent(v)
        if up_u == up_v: return
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]


ds = DisjointSet(7)
print("Testing Union By Rank\n")
ds.union_by_rank(1, 2)
ds.union_by_rank(2, 3)
ds.union_by_rank(4, 5)
ds.union_by_rank(6, 7)
ds.union_by_rank(5, 6)

if ds.find_parent(3) == ds.find_parent(7):
    print("Same parents")
else:
    print("Not same parents")

ds.union_by_rank(3, 7)

if ds.find_parent(3) == ds.find_parent(7):
    print("Same parents")
else:
    print("Not same parents")


ds2 = DisjointSet(7)
print("\n\nTesting Union By Size\n")
ds2.union_by_size(1, 2)
ds2.union_by_size(2, 3)
ds2.union_by_size(4, 5)
ds2.union_by_size(6, 7)
ds2.union_by_size(5, 6)

if ds2.find_parent(3) == ds2.find_parent(7):
    print("Same parents")
else:
    print("Not same parents")

ds2.union_by_size(3, 7)

if ds2.find_parent(3) == ds2.find_parent(7):
    print("Same parents")
else:
    print("Not same parents")