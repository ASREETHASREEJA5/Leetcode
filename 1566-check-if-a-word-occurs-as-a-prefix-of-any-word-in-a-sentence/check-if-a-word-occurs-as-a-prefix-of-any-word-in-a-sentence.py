class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        for i in l:
            if searchWord == i[:len(searchWord)]:
                return l.index(i)+1
        return -1
        