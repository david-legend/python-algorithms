class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words.sort(key=len, reverse=True)
        s = words[0] + "#"

        for i in range(1, len(words)):
            count = 0
            curr_word = words[i] + "#"
            if curr_word in s:
                count = 1
            if count == 0:
                s += curr_word

        return len(s)


class Trie:
    def __init__(self):
        self.root = dict()
        self.tail_nodes = []
    
    def insert(self, word):
        curr = self.root
        for i in range(len(word)-1, -1, -1):
            char = word[i]
            if char not in curr:
                curr[char] = dict()

            curr = curr[char]
        self.tail_nodes.append((curr, len(word) + 1))
    
    

def minimumLengthEncoding(words):
    unique_words = set(words)
    trie = Trie()

    for word in unique_words:
        trie.insert(word)
    
    min_length = 0
    for node, count in trie.tail_nodes:
        if len(node) == 0:
            min_length += count

    return min_length

print(minimumLengthEncoding(["time","me","bell", "el"])) #13
print(minimumLengthEncoding(["time","me","bell", "ll", "ti"])) #13
print(minimumLengthEncoding(["time","time","time", "time", "time"])) #5