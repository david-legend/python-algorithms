def longestWord(words):
    words.sort()
    longest_word, built_words = "", set()
    for word in words:
        if len(word) == 1 or word[:len(word) - 1] in built_words:
            if len(word) > len(longest_word):
                longest_word = word
            built_words.add(word)
    
    return longest_word