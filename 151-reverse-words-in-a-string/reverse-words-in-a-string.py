class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split() #make a list
        index = -1
        reverse = ""
        while abs(index) <= len(words): #go backwards through it to make a string
            if index == -1: #prevents leading whitespace
                reverse = words[index]
            else:
                reverse = reverse + " " + words[index]
            index -= 1
        return reverse
        