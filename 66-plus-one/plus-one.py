class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ""
        count = 0
        while count < len(digits):
            number = number + str(digits[count])
            count += 1
        total = int(number) + 1
        converted = [int(char) for char in str(total)]
        return converted
        