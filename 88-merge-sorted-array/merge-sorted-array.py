class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new1 = nums1[:(m)] #switch to list without extra elements
        new1.extend(nums2) #merge the lists
        new1.sort() #sort it
        nums1[:] = new1 #replace with sorted list
 

        
        