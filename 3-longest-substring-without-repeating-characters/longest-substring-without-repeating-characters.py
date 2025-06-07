class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        start = 0
        end = 0
        max = 0
        for each in s:
            if len(sub) == 0:
                sub = each
            elif each in sub:
                mark = sub.index(each) + 1
                sliced = sub[mark:]
                sub = sliced + each
            elif each not in sub:
                sub = sub + each
            if len(sub) > max:
                max = len(sub)
        return max
        