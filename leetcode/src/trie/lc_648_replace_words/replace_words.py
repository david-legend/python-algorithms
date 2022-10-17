class TrieNode: 
    def __init__(self):
        self.children, self.end_of_word = {}, False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end_of_word = True
    
    def replace(self, word):
        curr = self.root
        for idx, char in enumerate(word):
            if char not in curr.children:
                return word
            curr = curr.children[char]
            if curr.end_of_word:
                return word[:idx+1]
        return word


def replaceWords(dictionary, sentence):
    trie = Trie()
    for word in dictionary:
        trie.add_word(word)

    words = sentence.split(" ")
    for idx, word in enumerate(words):
        words[idx] = trie.replace(word)

    return " ".join(words)