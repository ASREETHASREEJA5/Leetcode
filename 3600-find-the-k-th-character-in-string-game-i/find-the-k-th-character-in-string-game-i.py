class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word)<k:
            curr_s = ""
            for i in word:
                if i == "z":
                    curr_s+="a"
                else:
                    curr_s+=chr(ord(i)+1)
            word+=curr_s
        return word[k-1]