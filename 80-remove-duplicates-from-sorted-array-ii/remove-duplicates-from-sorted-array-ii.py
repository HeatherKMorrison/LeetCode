class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        totals = {}
        max_length = len(nums) 
        count = 0
        while count < max_length: 
            item = nums[count] 
            if item not in totals:
                totals[item] = 1
            else:
                totals[item] += 1
            if totals[item] < 3:
                nums.append(item)
            count += 1
        nums[:] = nums[max_length:]
        k = len(nums)
        padding = max_length - len(nums)
        count = 0
        while count < padding:
            nums.append(0)
            count += 1
        return k


                  
        
