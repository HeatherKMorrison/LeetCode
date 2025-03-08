class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split() #divide into list
        return len(words[-1]) #return length of last word