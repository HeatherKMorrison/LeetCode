class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = 0
        final = ""
       
        if len(word1) > len(word2):#find the length of the longest string
            length = len(word1)
        else:
            length = len(word2)
        count = 0

        while count < length: #weave the two strings together placing excess of the longest at the end
            if count < len(word1):
                final = final + word1[count]
            if count < len(word2):
                final = final + word2[count]
            count += 1
        return final