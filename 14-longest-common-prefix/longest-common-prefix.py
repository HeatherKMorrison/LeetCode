class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 1
        prefix = strs[0] #grab first string
        while count < len(strs):
            while strs[count].startswith(prefix) == False and len(prefix) != 0: #increment backwards until we have a match or nothing
                prefix = prefix[:-1]
            count += 1
        return prefix