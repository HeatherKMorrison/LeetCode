class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_repeat = len(nums)/2 #number we need to beat
        count = 0
        current = None
        inventory = {}
        major = None
        while count < len(nums): #count the number of times we get an integer until we beat the number
            current = nums[count]
            if current in inventory:
                inventory[current] += 1
                if inventory[current] > major_repeat:  
                    major = current #we found our number
                    break 
            else:
                inventory[current] = 1
            count += 1
        if major == None: #edge case with one element
           major = nums[0]
        return major
        