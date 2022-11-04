class TrieNode:
    def __init__(self):
        self.children, self.val = {}, 0
        self.end_of_word = False

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True
        curr.val = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        map_sum = 0
        for char in prefix:
            if char not in curr.children:
                return map_sum
            curr = curr.children[char]
        map_sum += curr.val
        map_sum = self.dfs(curr, map_sum)
        return map_sum

    def dfs(self, node, map_sum):
        for child in node.children.values():
            map_sum += child.val
            map_sum = self.dfs(child, map_sum)
        return map_sum



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert("apple",3)
# print(obj.sum("ap"))
# obj.insert("app",2)
# print(obj.sum("ap"))
# param_2 = obj.sum(prefix)


obj2 = MapSum()
obj2.insert("apple",3)
obj2.insert("ap",1)
print(obj2.sum("ap"))
obj2.insert("app",2)
print(obj2.sum("ap"))
obj2.insert("app",2)
print(obj2.sum("ap"))