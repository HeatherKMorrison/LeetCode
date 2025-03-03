class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        current = nums[0] #get the first value
        new_list = [nums[0]] #start new list of unique numbers

        while counter < len(nums):
            if nums[counter] != current:
                new_list.append(nums[counter]) #add unique numbers to new list
        
            current = nums[counter]
            counter += 1
        
        nums[:] = new_list #replace with unique list of integers
        return len(nums)