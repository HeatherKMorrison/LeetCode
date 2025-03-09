class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 1
        prefix = strs[0]
        while count < len(strs):
            while strs[count].startswith(prefix) == False and len(prefix) != 0:
                prefix = prefix[:-1]
            count += 1
        return prefix