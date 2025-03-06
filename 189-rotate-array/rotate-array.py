class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) #makes sure we wrap correctly regardless of length of k in respect to nums
        nums[:] = nums[-k:] + nums[:-k] #swap them
        