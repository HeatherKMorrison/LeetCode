class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        index = -1
        reverse = ""
        while abs(index) <= len(words):
            if index == -1:
                reverse = words[index]
            else:
                reverse = reverse + " " + words[index]
            index -= 1
        return reverse
        