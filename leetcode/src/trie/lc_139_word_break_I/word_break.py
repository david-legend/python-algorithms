class TrieNode:
    def __init__(self):
        self.children, self.end = {}, False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo = {}
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
    
    def find(self, word):
        curr = self.root
        for i, char in enumerate(word):
            if char not in curr.children: return False
            
            if curr.children[char].end:
                remaining_word = word[i+1:]
                if remaining_word not in self.memo:
                    self.memo[remaining_word] = self.find(remaining_word)

                if self.memo[remaining_word]:
                    return True

            curr = curr.children[char]
        return curr.end

def wordBreak(s, wordDict):
    trie = Trie()
    for word in wordDict:
        trie.insert(word)
    
    return trie.find(s)


print(wordBreak("leetcode", ["leet", "code"]))