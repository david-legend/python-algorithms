class TrieNode:
    def __init__(self):
        self.children, self.index = {}, -1
        self.palindrom_idx = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, index):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            char = word[i]
            if self.is_palindrome(word, 0, i):
                curr.palindrom_idx.append(index)
                
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.index = index
        curr.palindrom_idx.append(index)

    def search(self, word, index, result):
        curr = self.root
        for i in range(len(word)):
            char = word[i]

            if curr.index >= 0 and curr.index != index and self.is_palindrome(word, i, len(word) - 1):
                result.append([index, curr.index])

            if char not in curr.children:
                return
            curr = curr.children[char]
        
        for j in curr.palindrom_idx:
            if index != j:
                result.append([index, j])
        
    def is_palindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]: return False
            left += 1
            right -= 1
        return True


def palindromePairs(words):
    trie = Trie()

    for i, word in enumerate(words):
        trie.insert(word, i)
    
    result = []
    for i, word in enumerate(words):
        trie.search(word, i, result)
    
    return result


print(palindromePairs(["lls", "s"]))
    