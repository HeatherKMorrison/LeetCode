class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        k = len(nums)

        #calculate length of final list
        while counter < len(nums):
            if nums[counter] == val:
                k -= 1
            counter += 1
        val_count = len(nums) - k
        nums[:] = [num for num in nums if num != val] #remove val from list
        nums.extend([None] * val_count) #add None as filler at the end
        return k