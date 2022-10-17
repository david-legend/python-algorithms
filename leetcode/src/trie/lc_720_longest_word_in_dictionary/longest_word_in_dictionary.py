class TrieNode:
    def __init__(self):
        self.children, self.end_of_word = {}, False

class Trie: 
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True
    
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            if not curr.end_of_word:
                return False
        return curr.end_of_word

def longestWord(words):
    trie = Trie()
    longest_word = ""
    for word in words:
        trie.insert(word)
    
    for word in words:
        if trie.search(word):
            if len(word) > len(longest_word):
                longest_word = word
            elif len(word) == len(longest_word):
                longest_word = word if word < longest_word else longest_word
    
    return longest_word