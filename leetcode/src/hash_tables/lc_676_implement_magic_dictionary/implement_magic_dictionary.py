from collections import defaultdict

class MagicDictionary:
    def __init__(self):
        self.map = defaultdict(list)

    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            key = len(word)
            self.map[key].append(word)

    def search(self, searchWord: str) -> bool:
        key = len(searchWord)
        if key not in self.map: return False

        for word in self.map[key]:
            count = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]: count += 1
                if count > 1: break
            if count == 1: return True
        return False

dict = MagicDictionary()
dict.buildDict(["hello","hallo","leetcode"])
print(dict.search("hello")) #True
print(dict.search("hhllo")) #True
print(dict.search("hell")) #False
print(dict.search("leetcoded")) #False