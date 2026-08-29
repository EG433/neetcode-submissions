class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        l, r = 0, 0
        for num in nums:
            l, r = r, max(l + num, r)
        return r