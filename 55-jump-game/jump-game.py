class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        max = 0
        while count < len(nums):
            if nums[count] > max:
                max = nums[count]
            if count < len(nums) - 1 and nums[count] == 0 and max == 0:
                return False
            count += 1
            max -= 1
        return True
  